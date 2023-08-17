from typing import Generator


def simple_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


for number in simple_generator():
    print(number)

gen = simple_generator()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



