
from app.schemas.rooms import RoomCreate, RoomResponse, RoomStatus


class RoomService:
    def __init__(self):
        self._rooms_db = {}
        self._id_counter = 1

    def create_room(self, room_data: RoomCreate, host_id: int):
        room = RoomResponse(
            id=self._id_counter,
            status=RoomStatus.WAITING,
            host_id=host_id,
            current_players=1,
            max_players=room_data.max_players,
            name=room_data.name,
        )
        self._rooms_db[self._id_counter] = room
        self._id_counter += 1
        return room

    def get_room(self, room_id: int) -> RoomResponse | None:
        room = self._rooms_db.get(room_id)
        return room

    def get_available_rooms(self)->list[RoomResponse]:
        rooms=[ value for value in self._rooms_db.values() if value.status.value == RoomStatus.WAITING and value.current_players < value.max_players]
        return rooms

    def join_room(self, room_id: int) ->RoomResponse | None:
        room = self._rooms_db.get(room_id)
        if room is None:
            return None
        if room.status.value == RoomStatus.WAITING:
            raise ValueError("Room is not accepting players")
        if room.current_players >= room.max_players:
            raise ValueError("Room is full")
        room.model_copy()
        room.current_players += 1
        self._rooms_db[room_id] = room
        return room


room_service = RoomService()

