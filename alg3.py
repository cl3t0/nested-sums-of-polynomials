from typing import List


def nested_sum_of_polynomial(
    a: int,
    b: int,
    k: int,
    f_coefs: List[float],
) -> float:

    def func(x: int) -> int:
        # Horner's method for polynomial evaluation
        acc = f_coefs[-1]
        for coef in f_coefs[-2::-1]:
            acc *= x
            acc += coef
        return acc

    pascal = 1  # (k - 1 choose k - 1)
    res = 0
    for i in range(a, b + 1):
        res += pascal * func(a + b - i)
        pascal *= (k + i - a) / (i - a + 1)
    return res


# result = nested_sum_of_polynomial(
#     a=1,
#     b=100,
#     k=4,
#     f_coefs=[5, -1, 1, -5, -3, 3],  # Put your function coefficients here
# )

# print(int(result))
