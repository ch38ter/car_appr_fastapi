# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.dependencies import logger
from app.parameter.model import Withdraw
import sqlite3

# 实例化APIRouter实例
router = APIRouter(tags=["withdraw appr"])
# 注册具体方法
@router.post("/withdraw")
async def index(id: Withdraw, user: dict = Depends(token_check)):
    logger.info(id)
    logger.info(user)
    """
    默认访问链接
    """
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    if user['auth'] == '0':
        return {
            "code": 403,
            "msg": "Forbidden"}

    try:
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "UPDATE appr SET status = ? WHERE id = ?;"
        cs.execute(sql, ('1', id.id, ))
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
