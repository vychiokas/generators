from typing import Generator


def sequence(start_number: int = 100) -> Generator[int, int, None]:
    i = start_number
    while True:
        skip = yield i
        if skip:
            i += skip
        else:
            i += 1


def some_generator() -> Generator[int, int, None]:
    while True:
        received_value = yield
        print("Received:", received_value)


my_sequence = sequence(1)

print(f"got from 1st generator {next(my_sequence)}")
print(f"got from 1st generator {next(my_sequence)}")
print(f"got from 1st generator {my_sequence.send(5)}")

some_gen = some_generator()
print(f"got from 2nd generator {next(some_gen)}")
print(f"got from 2nd generator {some_gen.send('Hello world!')}")
