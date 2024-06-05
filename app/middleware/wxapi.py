import requests
from app.constant import APP_ID, APP_SECRET

def get_user_openid(js_code):
    session_type = 'authorization_code'
    res = requests.get('https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type={}'.format(APP_ID, APP_SECRET, js_code, session_type)).json()
    try:
        openid = res['openid']
        session_key = res['session_key']
    except Exception:
        return(None, None)
    else:
        return(openid, session_key)
