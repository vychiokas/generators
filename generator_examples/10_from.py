from typing import Generator

# yield from essentially is <for i in my_iterable: yield i>


def sub_generator() -> Generator[str, None, None]:
    yield "A"
    yield "B"


def simple_generator() -> Generator[str, None, None]:
    yield "Start"
    for item in sub_generator():
        yield item
    yield "End"


def main_generator() -> Generator[str, None, None]:
    yield "Start"
    yield from sub_generator()  # Delegates to sub_generator
    yield "End"


# Iterating over main_generator
for item in simple_generator():
    print(item)

print("-" * 20)

for item in main_generator():
    print(item)
