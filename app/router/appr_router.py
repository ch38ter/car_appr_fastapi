# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.parameter.model import AppForm
import sqlite3
from datetime import datetime, timezone
from app.dependencies import logger

# 实例化APIRouter实例
router = APIRouter(tags=["appr summit"])
# 注册具体方法
@router.post("/appr")
async def index(form: AppForm, user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    logger.info(form)
    logger.info(user)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    if user['auth'] == '0':
        return {
            "code": 403,
            "msg": "Forbidden"}

    name = form.user_applicant
    department = form.user_department
    reason = form.reason
    time_from = form.time_from
    time_to = form.time_to
    approver = form.user_approver
    cc = form.user_cc
    companions = form.companions
    time_summit = datetime.now(timezone.utc)
    try:
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "INSERT INTO appr (member_id, reason, start_time, end_time, companions, member_name, approver, cc, department, summit_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        cs.execute(sql, (user["userid"], reason, time_from, time_to, companions, name, approver, cc, department, time_summit))
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