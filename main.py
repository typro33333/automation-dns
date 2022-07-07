import uvicorn

from threading import Thread
from fastapi import FastAPI
from runbot.run import start_bot_telegram

# Routes
# from routes import users, items


if __name__ == '__main__':
  start_bot_telegram()
  # app = FastAPI()
  # app.include_router(users.router)
  # app.include_router(items.router)
  # uvicorn.run(app=app, host="0.0.0.0", port=8000)
