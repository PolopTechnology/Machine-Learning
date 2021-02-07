import numpy as np
cases = np.array([1, 2, 4, 5, 6])
i = 0
times = 0

res = []

for case in cases:
    i += 1
    if i == case:
        print("Clustering...")
        times += 1
    if times == 0:
        print("UnClustered")
        polus = np.split(cases, [case])
        res.append(polus)
    times = 0


print(res)