import uvicorn

from . import env


if __name__ == "__main__":
    uvicorn.run("flax.app.main:app", host="0.0.0.0", port=env.port, reload=env.debug)
