import asyncio

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from uvicorn import Config, Server

app = FastAPI()


def calculate_sum(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError
    return a + b


@app.get("/")
async def get_sum(a: int, b: int) -> JSONResponse:
    try:
        result = calculate_sum(int(a), int(b))
    except:
        return JSONResponse({"status": False, "result": "wrong request"})
    else:
        return JSONResponse({"status": True, "result": result})


@app.on_event("shutdown")
async def shutdown_event_http() -> None:
    for server in servers:
        server.should_exit = True


configs = [
    Config(
        app=app,
        host="0.0.0.0",
        port=8080,
    ),
]
servers = [Server(config) for config in configs]


async def run_uvicorn_servers() -> None:
    await asyncio.gather(*[server.serve() for server in servers])


if __name__ == "__main__":
    asyncio.run(run_uvicorn_servers())
