from typing import Generator

from utils import benchmark, materialize_generator


@benchmark
def file_reader_generator(file_name: str) -> Generator[str, None, None]:
    for row in open(file_name, "r", encoding="utf8"):
        yield row


@benchmark
def file_reader(file_name: str) -> str:
    file = open(file_name, "r", encoding="utf8")
    result = file.read().split("\n")
    return result


text_generator = file_reader_generator("data/Individual_Incident_2004.csv")
materialized_text = materialize_generator(text_generator)
text = file_reader("data/Individual_Incident_2004.csv")
