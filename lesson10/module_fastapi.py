from fastapi import FastAPI
from lesson10.users.users_router import router as router_users

app = FastAPI()
app.include_router(router_users)


@app.get("/")
async def start():
    return {"Hello": "World2"}


@app.get("/sum_{a}_{b}")
async def sum_of_two(a: int, b: int) -> int:
    return a+b
