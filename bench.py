import alg1
import alg2
import alg3
import alg4
import time
from typing import List, Callable


def measure(a: int, b: int, k: int, f_coefs: List[float]) -> Callable[[int], float]:
    def func(alg: int) -> float:
        f = [
            alg1.nested_sum_of_polynomial,
            alg2.nested_sum_of_polynomial,
            alg3.nested_sum_of_polynomial,
            alg4.nested_sum_of_polynomial,
        ][alg - 1]
        t0 = time.time()
        f(a, b, k, f_coefs)
        t1 = time.time()
        return t1 - t0

    return func
