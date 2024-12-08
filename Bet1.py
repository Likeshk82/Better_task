from typing import List, Dict

books = []
members = []

class Book:
    def __init__(self, id: int, title: str, author: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self) -> Dict:
        return {"id": self.id, "title": self.title, "author": self.author, "year": self.year}
    
class Member:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def to_dict(self) -> Dict:
        return {"id": self.id, "name": self.name, "email": self.email}
