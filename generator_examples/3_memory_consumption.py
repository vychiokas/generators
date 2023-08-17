from functools import wraps
import random
import sys
from dataclasses import dataclass
from typing import Generator, List
import time

import names


def benchmark(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        print(f"Memoy consumed: {sys.getsizeof(result)} bytes")
        return result
    return timeit_wrapper

@benchmark
def generator_materializer(g: Generator[int, None, None]):
    return list(g)


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
    for i in range(number):
        yield Person(names.get_full_name(), random.randint(1, 100))




people = create_people(1000)
people_generator = generate_people(1000)
materialized_people = generator_materializer(people_generator)
print(materialized_people)

