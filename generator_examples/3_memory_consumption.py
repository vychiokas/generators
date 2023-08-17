import random
import sys
from dataclasses import dataclass
from typing import List

import names


@dataclass
class Person:
    name: str
    age: int
    

def create_people(number: int) -> List[Person]:
    people = []
    for _ in range(number):
        people.append(Person(names.get_full_name(), random.randint(1, 100)))
        print(_)
    return people


people = create_people(1000)
print(sys.getsizeof(people))
