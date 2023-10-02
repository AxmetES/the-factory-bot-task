import logging
import json
import requests
import uvicorn


from datetime import date
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from db import get_db
from schemas import UserSchema, UserLogin
from auth import signJWT, decodeJWT
from jwt_bearer import JwtBearer
from config import settings


app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.get("/message/", dependencies=[Depends(JwtBearer())], tags=["message"])
def get_message(message_: str, jwt_token: str = Depends(JwtBearer()), db: Session = Depends(get_db)):
    cur_date = date.today()
    payload = decodeJWT(jwt_token)
    login = payload.get('userID')
    chat_id: str = crud.get_chat_id(login, db)
    message = f'Дата отправки: {cur_date}\nСообщение: {message_}'
    tg_msg: json = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    API_URL = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    r = requests.post(url=API_URL, json=tg_msg)
    if r.status_code == 200:
        logger.info(f'Message send to tg, login: {login}, message: {message_}')
        return {
            "message": "Message sent successfully"
        }
    elif r.status_code == 400:
        logger.exception(r.text)
        return {
            "message": f"{r.json()['description']}. Status code: {r.status_code}"
        }
    else:
        logger.exception(r.text)
        return {
            "message": f"Failed to send Telegram message. Status code: {r.status_code}"
        }


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema, db: Session = Depends(get_db)):
    try:
        user: UserSchema = crud.get_or_create_user(user, db)
        token: str = signJWT(user.login)
        return {
            "access token": token
        }
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))


@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        if crud.check_user(user, db):
            token: str = signJWT(user.login)
            return {
                "access token": token
            }
        else:
            return {
                "error": "Invalid login details!"
            }
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
