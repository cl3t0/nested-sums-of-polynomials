import matplotlib.pyplot as plt
import pandas as pd

plt.figure(1)
df1 = pd.read_csv("bench1.csv")
df1[df1.alg == 1].set_index("k")["time"].plot(label="Naive Sum")
df1[df1.alg == 2].set_index("k")["time"].plot(label="Memoized Sum")
df1[df1.alg == 3].set_index("k")["time"].plot(label="BCS")
df1[df1.alg == 4].set_index("k")["time"].plot(label="BCBTS")
plt.legend()
plt.ylabel("time (seconds)")
plt.savefig("assets/1.png")

plt.figure(2)
df2 = pd.read_csv("bench2.csv")
df2[df2.alg == 2].set_index("k")["time"].plot(label="Memoized Sum")
df2[df2.alg == 3].set_index("k")["time"].plot(label="BCS")
df2[df2.alg == 4].set_index("k")["time"].plot(label="BCBTS")
plt.legend()
plt.ylabel("time (seconds)")
plt.savefig("assets/2.png")

plt.figure(4)
df4 = pd.read_csv("bench4.csv")
df4[df4.alg == 3].set_index("b")["time"].rolling(50).mean().plot(label="BCS")
df4[df4.alg == 4].set_index("b")["time"].rolling(50).mean().plot(label="BCBTS")
plt.legend()
plt.ylabel("time (seconds)")
plt.savefig("assets/4.png")

plt.figure(3)
fig, ax = plt.subplots(2)
fig.tight_layout(pad=5.0)
df3 = pd.read_csv("bench3.csv")

df3[(df3.alg == 3) & (df3.test_name == "normal")].set_index("k")["time"].rolling(
    50
).mean().plot(label="BCS", ax=ax[0])
df3[(df3.alg == 4) & (df3.test_name == "normal")].set_index("k")["time"].rolling(
    50
).mean().plot(label="BCBTS", ax=ax[0])
ax[0].legend()
ax[0].set_ylabel("time (seconds)")
ax[0].title.set_text("b - a = 99, n = 5")

df3[(df3.alg == 3) & (df3.test_name == "big b")].set_index("k")["time"].rolling(
    50
).mean().plot(label="BCS", ax=ax[1])
df3[(df3.alg == 4) & (df3.test_name == "big b")].set_index("k")["time"].rolling(
    50
).mean().plot(label="BCBTS", ax=ax[1])
ax[1].legend()
ax[1].set_ylabel("time (seconds)")
ax[1].title.set_text("b - a = 999, n = 5")

fig.savefig("assets/3.png")
