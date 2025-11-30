from enum import Enum

from pydantic import BaseModel, Field


class RoomStatus(str, Enum):
    """Статусы комнаты"""

    WAITING = "waiting"
    IN_PROGRESS = "in_progress"
    FINISHED = "finished"


class RoomBase(BaseModel):
    """Базовая схема комнаты"""

    name: str = Field(..., min_length=3, max_length=50)
    max_players: int = Field(default=10, ge=4, le=20)


class RoomCreate(RoomBase):
    """Схема для создания комнаты"""

    pass


class RoomResponse(RoomBase):
    """Схема ответа комнаты"""

    id: int
    status: RoomStatus
    current_players: int
    host_id: int  # ID игрока, который является хостом комнаты

    class Config:
        from_attributes = True
