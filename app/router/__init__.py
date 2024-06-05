from app.router import default_router, demo_router, reg_router, history_router, appr_router, userinfo_router, userset_router, check_token
from app.router import getdepartlist_router, getapproverlist_router, getcclist_router, statistics_router, waitforsummit_router, getapprlist
from app.router import withdraw, allowappr, denyappr

# 定义路由列表
RegisterRouterList = [
    # default_router,
    # demo_router,
    reg_router,
    history_router,
    appr_router,
    check_token,
    getdepartlist_router,
    getapproverlist_router,
    getcclist_router,
    statistics_router,
    waitforsummit_router,
    getapprlist,
    withdraw,
    allowappr,
    denyappr,
    #######################Spared API below#########################
    userinfo_router,
    userset_router,
]