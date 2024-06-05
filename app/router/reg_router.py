from fastapi import APIRouter
from app.parameter.model import Reg
from app.middleware import get_user_openid
from app.dependencies import logger
import sqlite3
from datetime import datetime, timedelta, timezone
import jwt
from app.constant import STORED_TOKEN

router = APIRouter(tags=["User login and reg."])

@router.post('/login')
async def onLogin(reg: Reg):

    logger.info(reg)
    openid, session_key = get_user_openid(reg.code)
    logger.info(openid, session_key)
    if openid is not None:
        
        # 如果不存在用户就建立用户，否则就是老用户。
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "SELECT * FROM member WHERE wx_openid = '{}'".format(openid)
        cs.execute(sql)
        result = cs.fetchall()
        if len(result) == 0:
            now_time = datetime.now()
            au = '0'
            sql = "INSERT INTO member (wx_openid, create_time, lastlogin_time, authority) VALUES ('{}', '{}', '{}', '{}')".format(openid, now_time, now_time, au)
            cs.execute(sql)
            conn.commit()
            conn.close()

            logger.info("New User")
        else:
            conn.close()

            logger.info("Old User")
            update_login_time(openid)

        jwttoken = generate_token(openid)
        STORED_TOKEN.append(jwttoken)
        logger.info("Number of stored token: "+str(len(STORED_TOKEN)))
        return jwttoken
    else:
        # print('d')
        logger.error('get wx api openid error.')
def generate_token(openid: str) -> str:
    secret_key = 'ucue&83jv92KYn'
    # expiration = datetime.utcnow() + timedelta(minutes = 30)
    expiration = datetime.now(timezone.utc) + timedelta(minutes = 30)
    # print(expiration)
    payload = {"userid": openid, "exp": expiration}
    result = jwt.encode(payload, secret_key, algorithm="HS256")
    return result

def update_login_time(openid: str):
    with sqlite3.connect('./db/appr.db') as conn:
        cs = conn.cursor()
        sql = "UPDATE member SET lastlogin_time=? WHERE wx_openid=?"
        cs.execute(sql,(datetime.now(), openid))
        conn.commit()
