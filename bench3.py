from bench import measure
import pandas as pd

a = 1
f_coefs = [5, -1, 1, -5, -3, 3]
benchs = []
for k in range(1, 1000):
    test = measure(a=a, b=100, k=k, f_coefs=f_coefs)
    test_big_b = measure(a=a, b=1000, k=k, f_coefs=f_coefs)
    t3 = test(3)
    print(t3)
    t4 = test(4)
    print(t4)
    bench = {"a": a, "b": 100, "k": k, "f_coefs": str(f_coefs), "test_name": "normal"}
    benchs.append({**bench, "alg": 3, "time": t3})
    benchs.append({**bench, "alg": 4, "time": t4})

    t3_big_b = test_big_b(3)
    print(t3_big_b)
    t4_big_b = test_big_b(4)
    print(t4_big_b)
    bench = {"a": a, "b": 1000, "k": k, "f_coefs": str(f_coefs), "test_name": "big b"}
    benchs.append({**bench, "alg": 3, "time": t3_big_b})
    benchs.append({**bench, "alg": 4, "time": t4_big_b})

pd.DataFrame(benchs).to_csv("bench3.csv", index=None)
