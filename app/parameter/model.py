from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float


class Plaintext(BaseModel):
    group_method: str
    encrypt_key: str
    encrypt_data: str


class AppForm(BaseModel):
    wx_id: str
    user_department: str
    user_applicant: str
    reason: str
    time_from: str
    time_to: str
    user_approver: str
    user_cc: str
    companions: str

class Reg(BaseModel):
    code: str
    
class UserToken(BaseModel):
    id: str
    exp: str
    auth: str
    
class JWT(BaseModel):
    jwt: str

class UserInfo(BaseModel):
    id: str
    name: str
    authority: str
    
class TokenCheck(BaseModel):
    jwt: str
    
class HisYear(BaseModel):
    year: str
    
class Withdraw(BaseModel):
    id: str
    