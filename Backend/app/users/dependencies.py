from fastapi.security import HTTPBearer, HTTPBasicCredentials
from fastapi import Depends
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError

from app.exceptions import TokenExpiredException, IncorrectTokenFormatException
from app.users.auth_utilits import decode_jwt, ACCESS_TOKEN_TYPE, validate_user_from_payload, validate_token_type

http_bearer = HTTPBearer()


def get_current_payload(credentials: HTTPBasicCredentials = Depends(http_bearer)):
    try:
        payload = decode_jwt(token=credentials.credentials)
        return payload
    except ExpiredSignatureError:
        raise TokenExpiredException
    except InvalidTokenError:
        raise IncorrectTokenFormatException

async def get_current_user_from_access(payload: dict = Depends(get_current_payload)):
    validate_token_type(payload, ACCESS_TOKEN_TYPE)
    user = await validate_user_from_payload(payload)
    return user


