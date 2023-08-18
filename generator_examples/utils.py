import sys
import time
from functools import wraps
from typing import Any, Generator, List


def benchmark(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} s")
        print(f"Memory consumed: {sys.getsizeof(result)} bytes")
        return result

    return timeit_wrapper


@benchmark
def materialize_generator(g: Generator[Any, None, None]) -> List[Any]:
    return list(g)
