from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Game, User, Role

test = test()

app = FastAPI()

dbUsers: List[User] = [
    User(id=UUID("71a99779-9904-4a12-834d-8c38a08e45f2"), first_name="Alex", last_name="Nilsson", nickname="Gaston", roles=[Role.admin, Role.user]),
    User(id=uuid4(), first_name="Ekaterina", last_name="Glebova", nickname="Bela", roles=[Role.user])
]

dbGames: List[Game] = [
    Game(id=uuid4(), game_name="Catan", game_description="Cool game where the goal is to build your settlement!", rating=5),
    Game(id=uuid4(), game_name="Clank! Catacombs", game_description="Discover the dragons catacombs for treasures.", rating=3),
    Game(id=uuid4(), game_name="Fantasy Realms", game_description="Card game that is fun and fast to play.", rating=7),
    Game(id=uuid4(), game_name="Monopoly", game_description="It's monopoly.", rating=1),
    Game(id=uuid4(), game_name="Risk", game_description="Take over the world.", rating=4),
    Game(id=uuid4(), game_name="UNO", game_description="You know it, you hate that you love it.", rating=2),
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return dbUsers;

@app.get("/api/v1/games")
async def fetch_games():
    return dbGames;