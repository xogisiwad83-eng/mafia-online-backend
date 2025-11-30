from pydantic import BaseModel, EmailStr, Field


class PlayerBase(BaseModel):
    """Базовая схема игрока"""

    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr


class PlayerCreate(PlayerBase):
    """Схема для создания игрока"""

    password: str = Field(..., min_length=6)


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
