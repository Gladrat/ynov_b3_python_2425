from __future__ import annotations
from typing import TypedDict

str
int
float
bool

list
dict


class User(TypedDict):
    id: int
    name: str
    active: bool
    # Explication des imports sur les classes en cours de construction

    def compare_user(self, user: User):
        # do something
        # self.id == user.
        pass


def is_active(user: User) -> bool:
    return user["active"]


def square(n: int) -> int:
    return n*n


def mean(values: list[int]) -> float:
    return sum(values) / len(values)


if __name__ == "__main__":
    res = square(42)
    print(res)

    u: User = {
        "id": 12, 
        "name": "Geoffroy", 
        "active": True
    }

    is_active(u)
