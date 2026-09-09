from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


asheesh: Person = {"name": "Asheesh", "age": 28}

print(asheesh)
