# Wechat mini program backend developed by FastAPI.

# Structure
'''
├── README.md  #项目介绍
├── app
│   ├── __init__.py
│   ├── config  # 配置相关
│   │   └── __init__.py
│   ├── constant  # 常量相关
│   │   └── __init__.py
│   ├── dao # 封装查询数据的方法
│   │   └── __init__.py
│   ├── dependencies  # 封装被依赖函数
│   │   └── __init__.py
│   ├── middleware # 中间件
│   │   └── __init__.py
│   ├── models # 数据模型文件，和表结构对应
│   │   └── __init__.py
│   ├── router # 路由也可以理解controller
│   │   ├── __init__.py
│   │   ├── default_router.py # 默认接口
│   │   └── demo_router.py # 演示接口
│   ├── parameter # 声明参数对应的Pydantic模型
│   │   └── __init__.py
│   ├── service # 就具体业务实现逻辑
│   │   └── __init__.py
│   └── utils # 工具类
│       ├── __init__.py
│       └── str_util.py
├── main.py # 主文件
├── requirements.txt #依赖文件
├── tests # 单元测试目录
    ├── __init__.py
    └── local_test.py

'''