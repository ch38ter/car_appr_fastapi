# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.parameter.model import UserInfo
import sqlite3
from app.dependencies import logger

# 实例化APIRouter实例
router = APIRouter(tags=["set user name and auth"])
# 注册具体方法
@router.post("/userset")
async def index(form: UserInfo, user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    logger.info(user)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}

    if user['auth'] != '3':
        return {
            "code": 403,
            "msg": "Forbidden"}

    id = form.id
    name = form.name
    authority = form.authority

    try:
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "UPDATE member SET name = ?, authority = ? WHERE id = ?;"
        cs.execute(sql, (name, authority, id,))
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