from annotated_types import MinLen
from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated

class SUserAuth(BaseModel):
    email: EmailStr
    password: Annotated[str, MinLen(8)]

class SUserRegisterResponse(BaseModel):
    detail: str = 'The user has been registered successfully.'

class SUserLogoutResponse(BaseModel):
    detail: str = 'The user logout successfully.'

class STokenInfo(BaseModel):
    access_token: str
    refresh_token: str

class SRefreshToken(BaseModel):
    refresh_token: str