import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class PlayerBase(BaseModel):
    """Базовая схема игрока"""

    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr


class PlayerCreate(PlayerBase):
    """Схема для создания игрока"""

    password: str = Field(..., min_length=6)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not re.match(r"^[a-zA-Z0-9_]$", value):
            raise ValueError("Username must contain only letters, numbers and underscores")
        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        value = value.lower().strip()
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:

        if len(value) < 7 and len(value) > 120:
            raise ValueError("password must contain 8-120 characters long")
        if not re.match(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.match(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.match(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        return value

class PlayerUpdate(BaseModel):
    """Схема для обновления игрока"""

    username: str | None = Field(None, min_length=3, max_length=20)
    email: EmailStr | None = None


class PlayerResponse(PlayerBase):
    """Схема ответа игрока"""

    id: int
    rating: int
    games_played: int
    wins: int

    class Config:
        from_attributes = True
