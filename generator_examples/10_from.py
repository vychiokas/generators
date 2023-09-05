from typing import Generator


def sub_generator() -> Generator[str, None, None]:
    yield "A"
    yield "B"


def main_generator() -> Generator[str, None, None]:
    yield "Start"
    yield from sub_generator()  # Delegates to sub_generator
    yield "End"


# Iterating over main_generator
for item in main_generator():
    print(item)
