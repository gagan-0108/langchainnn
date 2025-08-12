from pydantic import BaseModel , Field , EmailStr
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email: EmailStr = "example@abc.in"
    cgpa: float = Field( gt=0 ,lt=10, default=4)

newStudent = {'name' : 'Gagan'}

student1 =  Student(**newStudent)

print( student1)