from typing import Generator

from utils import benchmark


@benchmark
def fib_gen():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1


# Careful - infinite generation.. Duuhh!
for number in fib_gen():
    print(number)
