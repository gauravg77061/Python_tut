from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool

input__data={'id':101,'name':'chaicode','is_active':True}
# input_data1={'id':102,'name':123,"is_active":True}
user=User(**input__data)
# user1=User(**input_data1)
print(user)
# print(user1)

