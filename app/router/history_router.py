# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.parameter.model import HisYear
import sqlite3
from app.dependencies import logger
# 实例化APIRouter实例
router = APIRouter(tags=["history of appr"])
# 注册具体方法
@router.post("/his")
async def index(year: HisYear, user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    logger.info(user)
    logger.info(year)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    else:
        year = year.year[0:4]
        try:
            with sqlite3.connect('./db/appr.db') as conn:
                cs = conn.cursor()
                sql = "SELECT member_id, reason, start_time, end_time, companions, member_name, approver, cc, department, summit_time, app_time, status FROM appr WHERE member_id = ? AND strftime('%Y', summit_time) = ?;"
                cs.execute(sql, (user['userid'], year, ))
                res = cs.fetchall()

            if not res:
                return {
                    "code": 404,
                    "msg": "No data found for the given user_id"
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
