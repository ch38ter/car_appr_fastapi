from fastapi import FastAPI, Depends, Header, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from app.router import RegisterRouterList
from app.dependencies import logger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 实例化
app = FastAPI(
    docs_url=None,
    redoc_url=None
)

logger.info("开始！！！")
# 加载路由 
for item in RegisterRouterList:
    # app.include_router(item.router, dependencies=[Depends(oauth2_scheme)])
    logger.info(f"加载路由：{item}")
    app.include_router(item.router)

logger.info("加载路由完成！！！")