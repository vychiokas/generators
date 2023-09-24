from typing import Dict, Generator, List


# Pipeline 1
FILE_PATH = "data/speech.txt"

file_lines = (line for line in open(FILE_PATH, "r", encoding="utf8"))
list_line = (s.rstrip().split(",") for s in file_lines)

next(list_line)
print(next(list_line))


# Pipeline 2


def transform_data(data: List[str]) -> Dict:
    # Do some data enriching and transformation
    ...


def send_data(data: List[str]) -> None:
    # send data somewhere
    ...


def data_sending_loop(some_data_generator: Generator) -> None:
    for line in some_data_generator:
        transformed_data = transform_data(line)
        send_data(transformed_data)


data_sending_loop(file_lines)
