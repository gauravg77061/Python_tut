from typing import Optional
from pydantic import BaseModel, Field
import re

class Emp(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Emp Name",
        examples=["Gaurav"]
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000,
    )



user = Emp(id=1, name='Gaurav', salary=20000)
print(user)
