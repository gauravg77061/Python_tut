from pydantic import BaseMode,field_validator,model_validator

class User(BaseMode):
    username:str
    
    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    
class SignupuData(BaseMode):
    passwrd:str
    confirm_password:str

    @model_validator(mode='after')
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values