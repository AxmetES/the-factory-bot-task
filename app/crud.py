import logging

import models
import schemas


def get_or_create_user(body: schemas.UserSchema, db):
    user = db.query(models.User).filter(models.User.username == body.username).first()
    if user:
        print(user.login)
        return user
    else:
        try:
            new_user = models.User(login=body.login,
                                   password=body.password,
                                   username=body.username)
            print(new_user.login)
            db.add(new_user)
            return new_user
        except Exception as e:
            db.rollback()
            logging.exception(e)


def check_user(data: schemas.UserLogin, db):
    user = db.query(models.User).filter(
        models.User.login == data.login,
        models.User.password == data.password
    ).first()
    if user:
        return True
    return False


def get_chat_id(login, db):
    user = db.query(models.User).filter(models.User.login == login).first()
    if user:
        return user.chat_id