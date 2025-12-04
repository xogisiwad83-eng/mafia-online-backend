
from fastapi import APIRouter, HTTPException

from app.schemas import RoomCreate, RoomResponse
from app.services.rooms import room_service

router = APIRouter(prefix="/rooms", tags=["Rooms"])

@router.post("/{user_id}", response_model=RoomResponse, status_code=201)
def create_room(room_data: RoomCreate, user_id: int):
    try:
        return room_service.create_room(room_data, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[RoomResponse])
def get_available_rooms():
    try:
        return room_service.get_available_rooms()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{room_id}", response_model=RoomResponse)
def get_room(room_id: int):
    try:
        return room_service.get_room(room_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{room_id}/join", response_model=RoomResponse)
def join_room(room_id: int):
    try:
        return room_service.join_room(room_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))









