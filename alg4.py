import numpy as np
from typing import List


def nested_sum_of_polynomial(a: int, b: int, k: int, f_coefs: List[float]) -> float:
    n = len(f_coefs) - 1
    coefs_vec = np.array([0, *f_coefs]).reshape(-1, 1)

    # calculating pascal triangle elements
    last_val = 1  # (b + k - a choose 0)
    for i in range(k):
        last_val *= (b + k - a - i) / (i + 1)

    # calculating base vector values
    base = [0, last_val]
    # (b + k - a choose k)
    for i in range(2, n + 2):
        base.append(base[i - 1] * (b + k + i - 1 - a) / (k + i - 1))
    base_vec = np.array(base).reshape(1, -1)

    # initializing omega matrix
    omega = np.zeros(shape=(n + 2, n + 2))
    omega[1, 1] = 1

    # calculating omega matrix
    for j in range(2, n + 2):
        for i in range(1, j + 1):
            omega[i, j] = (i - 1) * omega[i - 1, j - 1] - (i - a) * omega[i, j - 1]

    result = np.linalg.multi_dot([base_vec, omega, coefs_vec])
    return result[0, 0]


# result = nested_sum_of_polynomial(
#     a=1,
#     b=100,
#     k=4,
#     f_coefs=[5, -1, 1, -5, -3, 3],  # Put your function coefficients here
# )

# print(int(result))
