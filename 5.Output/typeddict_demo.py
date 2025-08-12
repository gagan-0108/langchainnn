from typing import TypedDict

class person (TypedDict):
    Name: str
    Age: int

new_person: person = { 'Name': "Gagan", "Age" : 18}

print ( new_person)