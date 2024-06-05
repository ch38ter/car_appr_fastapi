import jwt
from app.constant import STORED_TOKEN
from app.parameter.model import JWT
import sqlite3

def token_check(jwt_token: JWT):
    if jwt_token.jwt in STORED_TOKEN:
        
        secret_key = 'ucue&83jv92KYn'
        try:
            result = jwt.decode(jwt_token.jwt, secret_key, algorithms=['HS256'])
        except jwt.exceptions.ExpiredSignatureError:
            
            STORED_TOKEN.pop(jwt_token.jwt)

        else:
            userid = result['userid']
            level = check_level(userid)
            user = {
                    'userid': userid,
                    'auth': level
                }
            return user
    else:
        return None

def check_level(userid):

    conn = None
    try:
        conn = sqlite3.connect('./db/appr.db')
        cs = conn.cursor()
        sql = "SELECT authority FROM member WHERE wx_openid = ?;"
        cs.execute(sql, (userid,))
        result = cs.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
