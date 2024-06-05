import jwt

def verify_user_code(user_code):
    # 验证user_code的有效性
    #
    user_id = generate_user_id()
    
    token = generate_token(user_id)
    
    return token
    