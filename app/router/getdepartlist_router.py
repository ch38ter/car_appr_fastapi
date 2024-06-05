# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.constant import DEPARTMENTS
from app.dependencies import logger
# 实例化APIRouter实例
router = APIRouter(tags=["department list options"])
# 注册具体方法
@router.post("/getdepartlist")
async def index(user: dict = Depends(token_check)):
    logger.info(user)
    if user is None:
        return {
            "code": 401,
            "msg": "Unauthorized"}
    else:
        return {
            "code": 200,
            "msg": "success",
            "data": DEPARTMENTS}
