import re

from fastapi import APIRouter, status, Request, Header
from app.users.shemas import SUserAuth, STokenInfo, SUserRegisterResponse, SRefreshToken
from app.users.dao import UsersDao
from app.users.auth_utilits import get_password_hash, authentication, create_access_token, create_refresh_token, refresh
from app.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи'],
)

@router.post('/register/', status_code=status.HTTP_201_CREATED, response_model=SUserRegisterResponse)
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDao.add(email=user_data.email, hashed_password=hashed_password)
    return {'detail': 'The user has been registered successfully.'}

@router.post('/login/', response_model=STokenInfo)
async def jwt_login_user(user_data: SUserAuth):
    user = await authentication(user_data.email, user_data.password)
    if user is None:
        raise IncorrectEmailOrPasswordException

    access_token: str = create_access_token(user)
    refresh_token: str = create_refresh_token(user)
    await UsersDao.update_refresh_token(user_id=user.id, token=refresh_token)
    return STokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
    )

@router.post('/refresh/')
async def jwt_refresh_token(refresh_token: SRefreshToken):
    answer = await refresh(refresh_token=refresh_token.refresh_token)
    return answer