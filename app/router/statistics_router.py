# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.dependencies import logger
from datetime import datetime
import sqlite3

# 实例化APIRouter实例
router = APIRouter(tags=["Statistics of approval"])
# 注册具体方法
@router.post("/statistic")
async def index(user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    logger.info(user)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    else:
        now = datetime.now()
        current_month = now.strftime("%Y-%m")
        try:
            with sqlite3.connect('./db/appr.db') as conn:
                cs = conn.cursor()
                sql = "SELECT COUNT(*) FROM appr WHERE member_id = ?;"
                cs.execute(sql, (user['userid'], ))
                total_count = cs.fetchone()[0]
                sql = "SELECT COUNT(*) FROM appr WHERE member_id = ? AND strftime('%Y-%m', summit_time) = ?;"
                cs.execute(sql, (user['userid'], current_month))
                month_count = cs.fetchone()[0]

            return {
                "code": 200,
                "msg": "success",
                "data": {'total': total_count, 'month': month_count}
            }
        except sqlite3.Error as e:
            logger.error(e)
            return {
                "code": 500,
                "msg": "Database error!"
            }
