from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]= None 

Comment.model_rebuild()

comment =Comment(
    id=2,
    content="First comment",
    replies=[
        Comment(id=2,content="reply"),
        Comment(id=2,content='reply2'),
    ]
)

print(comment)
