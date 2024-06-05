# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
import sqlite3

# 实例化APIRouter实例
router = APIRouter(tags=["User information"])
# 注册具体方法
@router.post("/userinfo")
async def index(user: dict = Depends(token_check)):
    """
    默认访问链接
    """
    
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
        
    if user['auth'] != '3':
        return {
            "code": 403,
            "msg": "Forbidden"}
    try:
        with sqlite3.connect('./db/appr.db') as conn:
            cs = conn.cursor()
            sql = "SELECT * FROM member;"
            cs.execute(sql)
            res = cs.fetchall()
            name_list = [{"id": i[0], "name": i[1], "wx_unionid": i[2], "wx_appid": i[3],
                          "wx_openid": i[4], "title": i[5], "create_time": i[6],
                          "lastlogin_time": i[7], "authority": i[8]
                          } for i in res]
            return {
                "code": 200,
                "msg": "success",
                "data": name_list}

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return {
            "code": 500,
            "msg": f"Database error: {e}"
        }
