from typing import Generator, List


def square_numbers(numbers: List[int]) -> List[int]:
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number**2)
    return squared_numbers


def square_numbers_generator(numbers: List[int]) -> Generator[int, None, None]:
    for number in numbers:
        yield number**2


print(square_numbers([1, 2, 3]))

for number in square_numbers_generator([1, 2, 3]):
    print(number)

print(list(square_numbers_generator([1, 2, 3])))
