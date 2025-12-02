from fastapi import Depends
from typing import Annotated

from app.services.players import PlayerService, player_service
from app.services.rooms import RoomService, room_service

def get_player_service() -> PlayerService:
    """Зависимость для получения сервиса игроков"""
    return player_service


def get_room_service() -> RoomService:
    """Зависимость для получения сервиса комнат"""
    return room_service


PlayerServiceDep = Annotated[PlayerService, Depends(get_player_service)]
RoomServiceDep = Annotated[RoomService, Depends(get_room_service)]

class Pagination:
    def __init__ (self, skip: int, limit: int):
        self.skip = skip
        self.limit = limit


PaginationDep = Annotated[Pagination, Depends()]
