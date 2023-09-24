from typing import Generator

from utils import benchmark


@benchmark
def infinite_sequence() -> Generator[int, None, None]:
    num = 0
    while True:
        yield num
        num += 1


@benchmark
def fibonacci_sequence() -> Generator[int, None, None]:
    a, b = 0, 1
    count = 0
    while count < 10:  # while True: for infinite loop
        yield a
        a, b = b, a + b
        count += 1


# Careful - infinite generation.. Duuhh!
for number in fibonacci_sequence():
    print(number)

fibonacci = fibonacci_sequence()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
