from typing import List,Optional
from pydantic import BaseModel
class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address

address=Address(
    street="Rohini sec 7",
    city='New Delhi',
    postal_code = '110086'
)

user=User(
    id=1,
    name='Gaurav',
    address=address
)
print(user)

