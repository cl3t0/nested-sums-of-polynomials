from bench import measure
import pandas as pd

a = 1
f_coefs = [5, -1, 1, -5, -3, 3]
benchs = []
for b in range(100, 10000):
    test = measure(a=a, b=b, k=500, f_coefs=f_coefs)
    t3 = test(3)
    print(t3)
    t4 = test(4)
    print(t4)
    bench = {"a": a, "b": b, "k": 500, "f_coefs": str(f_coefs)}
    benchs.append({**bench, "alg": 3, "time": t3})
    benchs.append({**bench, "alg": 4, "time": t4})

pd.DataFrame(benchs).to_csv("bench4.csv", index=None)
