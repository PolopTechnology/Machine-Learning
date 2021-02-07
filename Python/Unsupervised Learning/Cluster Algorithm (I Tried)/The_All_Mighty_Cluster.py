cases = [1,2,4,5,6,9,10]
cluster1 = []
cluster2 = []
i = 0
times = 0

for case in cases:
    i += 1
    if i == case:
        print("Clustering...")
        cluster1.append(case)
        times += 2
    if times == 0:
        print("UnClustered")
        cluster2.append(case)
    times -= 1


print(cluster1)
print(cluster2)




