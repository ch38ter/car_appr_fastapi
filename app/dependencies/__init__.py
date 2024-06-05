from app.dependencies.token import token_check
import logging

logger = logging.getLogger("wxmp_fastapi")
fh = logging.FileHandler("/home/log/wxmp.log", mode="a")
ff = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
fh.setFormatter(ff)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)