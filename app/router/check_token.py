# 导入APIRouter
from fastapi import APIRouter, Depends
from app.parameter.model import TokenCheck
from app.dependencies import token_check
from app.dependencies import logger
from app.constant import STORED_TOKEN

# 实例化APIRouter实例
router = APIRouter(tags=["check token valid"])
# 注册具体方法
@router.post("/checktoken")
async def index(user: dict = Depends(token_check)):
    logger.info(user)
    if user is not None:
        logger.info('token valid')
        return {"status": 'true', "message": 'token valid', "auth": user['auth']}
        
    else:
        logger.info('token invalid')
        return {"status": 'false', "message": 'token invalid'}
