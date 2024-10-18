from fastapi import HTTPException, status

class BaseException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

# Каталог
class ProductNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail="Product not found."

# Пользователи
class UserAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'A user with such an email exists.'

class IncorrectEmailOrPasswordException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Invalid email or password.'

class TokenExpiredException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail='The token has expired.'

class TokenAbsentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'The access token is missing.'

class IncorrectTokenFormatException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Invalid token format.'

class TokensDoesNotMatch(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Invalid token. Please log in again.'

class UserIsNotPresentException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED

class NotValidTokenTypeException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, invalid_token_type: str, excepted_token_type: str):
        self.detail = f'Invalid token type {invalid_token_type!r}, excepted {excepted_token_type!r}.'
        super().__init__(status_code=self.status_code, detail=self.detail)
