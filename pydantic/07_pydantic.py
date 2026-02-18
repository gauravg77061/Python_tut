from pydantic import BaseModel,field_validator,model_validator
from datetime import datetime

class Person(BaseModel):
    firstName:str
    lastName:str

    @field_validator('firstName','lastName')
    def name_must_be_capiital(cls,v):
        if not v.istitle():
            raise ValueError('Name must be capitilized')
        return v

#data trasnformation ->lower case
class User(BaseModel):
    email:str

    @field_validator('email')
    def normalize_email(cls,v):
        return v.lower().strip()
    
class product(BaseModel):
    price:str

    @field_validator('price',mode='before')
    def normalize_price(cls,v):
        if isinstance(v,str):
            return float(v.replace('$',''))
        return v
class Range(BaseModel):
    start_date:datetime
    end_date:datetime

    @model_validator(model='after')
    def validate_date_ranges(cls,values):
        if values.start_date >=values.end_date:
            raise ValueError('end date must be after end date')

user1=User(email='Gaurav@gmail.com')
print(user1)