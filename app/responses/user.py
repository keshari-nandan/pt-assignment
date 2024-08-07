from pydantic import EmailStr, BaseModel
from app.responses.base import BaseResponse


class UserResponse(BaseResponse):
    id: int
    name: str
    email: EmailStr
    is_active: bool


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str = "Bearer"
