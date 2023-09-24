from typing import Generator
import sqlite3
import os


DATABASE_NAME = "demo.db"
TABLE_NAME = "test"


def generate_database_records(
    cursor: sqlite3.Cursor, table_name: str = TABLE_NAME, batchsize: int = 2
) -> Generator[int, None, None]:
    cursor.execute(f"select * from {table_name}")
    while True:
        results = cursor.fetchmany(batchsize)
        if not results:
            break
        for result in results:
            yield result


def create_database_if_not_exist() -> None:
    if not os.path.isfile(DATABASE_NAME):
        conn = sqlite3.connect(DATABASE_NAME)
        conn.execute(f"create table {TABLE_NAME} (label str, val int)")
        data = [
            ("a", 1),
            ("a", 2),
            ("b", 9),
            ("b", 10),
            ("b", 11),
            ("c", 12),
            ("c", 13),
            ("c", 14),
        ]
        conn.executemany("insert into test values (?, ?)", data)
        conn.commit()


if __name__ == "__main__":
    create_database_if_not_exist()

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    my_generator = generate_database_records(cursor=cursor, batchsize=5)
    for result in my_generator:
        print(result)
