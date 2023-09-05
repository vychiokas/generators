from typing import Union

from utils import benchmark


@benchmark
def fib_gen():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1


@benchmark
def double(number: Union[int, float]):
    yield number**2


# Careful - infinite generation.. Duuhh!
for number in double(fib_gen()):
    print(number)
