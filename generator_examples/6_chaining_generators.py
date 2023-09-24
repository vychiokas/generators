from typing import Generator

from utils import benchmark


@benchmark
def fib_gen() -> Generator[int, None, None]:
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1


@benchmark
def double(number_generator: Generator[int, None, None]):
    for num in number_generator:
        yield num * num


for number in double(fib_gen()):
    print(number)
