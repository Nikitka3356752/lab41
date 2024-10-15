from fastapi import FastAPI
from web_app import api_router
from uvicorn import Config, Server

if __name__ == '__main__':
    app = FastAPI()
    app.include_router(api_router)
    config = Config(app=app, host="localhost", port=8080)
    server = Server(config)
    server.run()
