def cost_function(location, data_points):
    broken = False
    step1 = location
    step2 = location
    while True:
        step1 -= 1
        step2 += 1
        for x in data_points:
            if x == step1 or x == step2:
                print(str(location) + " is closest to " + str(x))
                broken = True
        if broken == True:
            break

loc = 5
data = [1, 3, 7, 14, 23]
cost_function(loc, data)
