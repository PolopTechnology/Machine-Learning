cases = [1, 2, 3, 4, 5, 7, 8, 9, 12, 10, 32]
cluster1 = []
cluster2 = []
i = 0
times = 0

for case in cases:
    i += 1
    if i == case:
        print("Clustering...")
        cluster1.append(case)
        times += 1
    if times == 0:
        print("UnClustered")
        cluster2.append(case)
    times = 0


print(cluster1)
print(cluster2)
