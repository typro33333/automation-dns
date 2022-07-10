import uvicorn

from threading import Thread
from fastapi import FastAPI
from runbot.run import start_bot_telegram
import sys, os

# Routes
# from routes import users, items


if __name__ == '__main__':
  try:
    start_bot_telegram()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
  # app = FastAPI()
  # app.include_router(users.router)
  # app.include_router(items.router)
  # uvicorn.run(app=app, host="0.0.0.0", port=8000)
