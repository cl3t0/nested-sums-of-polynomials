from bench import measure
import pandas as pd

a = 1
b = 100
f_coefs = [5, -1, 1, -5, -3, 3]
benchs = []
for k in range(1, 5):
    test = measure(a=a, b=b, k=k, f_coefs=f_coefs)
    t1 = test(1)
    print(t1)
    t2 = test(2)
    print(t2)
    t3 = test(3)
    print(t3)
    t4 = test(4)
    print(t4)
    bench = {"a": a, "b": b, "k": k, "f_coefs": str(f_coefs)}
    benchs.append({**bench, "alg": 1, "time": t1})
    benchs.append({**bench, "alg": 2, "time": t2})
    benchs.append({**bench, "alg": 3, "time": t3})
    benchs.append({**bench, "alg": 4, "time": t4})

pd.DataFrame(benchs).to_csv("bench1.csv", index=None)
