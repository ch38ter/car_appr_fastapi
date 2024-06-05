# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.dependencies import logger
import sqlite3

# 实例化APIRouter实例
router = APIRouter(tags=["get appr list"])
# 注册具体方法
@router.post("/apprlist")
async def index(user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    logger.info(user)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    if user['auth'] == '0' or user['auth'] == '1':
        return {
            "code": 403,
            "msg": "Forbidden"}

    try:
        with sqlite3.connect('./db/appr.db') as conn:
            cs = conn.cursor()
            sql = "SELECT name FROM member WHERE wx_openid = ?;"
            cs.execute(sql, (user['userid'],) )
            name = cs.fetchone()[0]
            
            sql = "SELECT member_id, reason, start_time, end_time, companions, member_name, approver, cc, department, summit_time, app_time, id FROM appr WHERE status = '0' AND approver = ?;"
            cs.execute(sql, (name,) )
            res = cs.fetchall()

        if not res:
            return {
                    "code": 404,
                    "msg": "No data found."
                }
                
        return {
                "code": 200,
                "msg": "success",
                "data": res
            }
    except sqlite3.Error as e:
        logger.error(e)
        return {
                "code": 500,
                "msg": "Database error!"
            }
