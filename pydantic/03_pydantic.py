from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id:int
    items:List[str]
    quant:Dict[str,int]

class Blog(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None
    #blog can have image url its not mandatory
    # if image is there then url should be string 

cart_data={
    "user_id":123,
    "items":["laptop","mouse","keyboard"],
    "quant": {"laptop":1,"mouse":2,"keyboard":3}
}
cart=Cart(**cart_data)



