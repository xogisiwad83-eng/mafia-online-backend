from fastapi import APIRouter, HTTPException

from app.schemas.players import PlayerCreate, PlayerResponse, PlayerUpdate
from app.services.players import player_service

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/", response_model=PlayerResponse, status_code=201)
def create_player(player_data: PlayerCreate):
    try:
        return player_service.create_player(player_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int):
    player = player_service.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.patch("/{player_id}", response_model=PlayerResponse)
def update_player(player_id: int, player_data: PlayerUpdate):
    player = player_service.update_player(player_id, player_data)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@router.delete("/{player_id}", status_code=204)
def delete_player(player_id: int):
    success = player_service.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")
