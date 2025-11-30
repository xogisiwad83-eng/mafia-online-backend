from app.schemas.players import PlayerCreate, PlayerResponse, PlayerUpdate


class PlayerService:
    def __init__(self):
        self._players_db = {}
        self._id_counter = 1

    def create_player(self, player_data: PlayerCreate) -> PlayerResponse:
        if any(p.username == player_data.username for p in self._players_db.values()):
            raise ValueError("Username already exists")
        if any(p.email == player_data.email for p in self._players_db.values()):
            raise ValueError("Email already exists")

        player = PlayerResponse(
            id=self._id_counter,
            username=player_data.username,
            email=player_data.email,
            rating=1000,
            games_played=0,
            wins=0,
        )

        self._players_db[self._id_counter] = player
        self._id_counter += 1
        return player

    def get_player(self, player_id: int) -> PlayerResponse | None:
        return self._players_db.get(player_id)

    def get_all_players(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> list[PlayerResponse]:
        if skip < 0 or limit <= 0:
            raise ValueError("Invalid skip or limit values")
        if skip >= len(self._players_db):
            return []
        players = list(self._players_db.values())
        return players[skip: skip + limit]

    def update_player(
        self,
        player_id: int,
        player_data: PlayerUpdate
    ) -> PlayerResponse | None:
        player = self.get_player(player_id=player_id)
        if not player:
            return None
        update_data = player_data.model_dump(exclude_unset=True)
        updated_player = player.model_copy(update=update_data)
        self._players_db[player_id] = updated_player
        return updated_player

    def delete_player(self, player_id: int) -> bool:
        if player_id in self._players_db:
            del self._players_db[player_id]
            return True
        return False


player_service = PlayerService()
