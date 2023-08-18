import random
from dataclasses import dataclass
from typing import Generator, List

import names

from utils import benchmark, materialize_generator


@dataclass
class Person:
    name: str
    age: int


@benchmark
def create_people(number: int) -> List[Person]:
    people = []
    for _ in range(number):
        people.append(Person(names.get_full_name(), random.randint(1, 100)))
    return people


@benchmark
def generate_people(number: int) -> Generator[int, None, None]:
    for _ in range(number):
        yield Person(names.get_full_name(), random.randint(1, 100))


people_list = create_people(1000)

people_generator = generate_people(1000)
materialized_people = materialize_generator(people_generator)
