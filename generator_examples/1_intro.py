from typing import Generator, Iterator

# yield available since python 2.2


def simple_generator() -> Generator[int, None, None]:
    yield 1
    yield 2
    yield 3


#  a bit less verbose type annotation for simple generator
def another_simple_generator() -> Iterator[int]:
    yield 4
    yield 5
    yield 6


for number in simple_generator():
    print(number)

gen = simple_generator()
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
