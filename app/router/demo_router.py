# 导入APIRouter
from fastapi import APIRouter, Depends
from app.dependencies import token_check
from app.parameter.model import UserToken
# 实例化APIRouter实例
router = APIRouter(tags=["demo路由"])
# 注册具体方法
@router.get("/demo")
async def index(UserId: str = Depends(token_check)):
    """
    默认访问链接
    """
    if UserId is not None:
        print(UserId)
        return {
            "code": 200,
            "msg": "Hello " + UserId,
            "remark": "If you get the message, FastAPI is running!"
        }