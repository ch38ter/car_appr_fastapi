# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.dependencies import logger
from app.parameter.model import Withdraw
import sqlite3
from datetime import datetime

# 实例化APIRouter实例
router = APIRouter(tags=["allow appr"])
# 注册具体方法
@router.post("/allowappr")
async def index(id: Withdraw, user: dict = Depends(token_check)):
    now_time = datetime.now()
    logger.info(id)
    logger.info(user)

    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    if user['auth'] == '0' or user["auth"] == '1':
        return {
            "code": 403,
            "msg": "Forbidden"}

    try:
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "SELECT name FROM member WHERE wx_openid = ?;"
        cs.execute(sql, (user['userid'], ))
        user_name = cs.fetchone()[0]
        sql = "UPDATE appr SET status = ?, app_time = ?, approver = ? WHERE id = ?;"
        cs.execute(sql, ('2', now_time, user_name, id.id, ))
        conn.commit()
    except sqlite3.Error as e:
        logger.error(e)
        return {
            "code": 500,
            "msg": "Database error!"
        }
    finally:
        conn.close()
    return {
        "code": 200,
        "msg": "success",
    }
