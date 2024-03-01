from typing import List


def nested_sum_of_polynomial(
    a: int,
    b: int,
    k: int,
    f_coefs: List[float],
) -> float:
    mem = {}

    def func(x: int) -> int:
        # Horner's method for polynomial evaluation
        acc = f_coefs[-1]
        for coef in f_coefs[-2::-1]:
            acc *= x
            acc += coef
        return acc

    def recursive_sum(x: int, k: int) -> float:
        if mem.get((x, k)) is not None:
            return mem[(x, k)]

        res = (
            func(x) if k == 0 else sum(recursive_sum(i, k - 1) for i in range(a, x + 1))
        )
        mem[(x, k)] = res
        return res

    return recursive_sum(b, k)


# result = nested_sum_of_polynomial(
#     a=1,
#     b=100,
#     k=4,
#     f_coefs=[5, -1, 1, -5, -3, 3],  # Put your function coefficients here
# )

# print(int(result))
