import numpy
cases = numpy.array([1, 2, 4, 5])
times = 1
for case in cases:
    if not times == int(case):
        sp = numpy.split(cases, [4])
        times += 1
    times += 1
print(sp)
