from typing import Generator


def sequence(start_number: int = 100) -> Generator[int, int, None]:
    i = start_number
    while True:
        print("entering loop")
        skip = yield i
        print(f"skip is {skip}")
        if skip:
            i += skip
        else:
            i += 1
        print(f"i is {i}")


def some_generator():
    while True:
        received_value = yield
        print("Received:", received_value)
        

my_sequence = sequence(1)

print(next(my_sequence))
print(next(my_sequence))
print(my_sequence.send(5))


some_gen = some_generator()
print(next(some_gen))
print()