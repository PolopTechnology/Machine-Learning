# WARNING: This is what I understood about cost functions #
# Which is basically trying to get to a point while losing #
# The least possible. That may be wrong but IDK #

points = [1, 6, 8, 13]  #Data points
location = int(input()) #Current location of user
step1 = location #Step back
step2 = location #Step Forward
broken = False #Checks wether point reached

while True:  #loop
    step1 -= 1
    for x in points:
        if x == step1:  #takes step back. if location == to a point, print that that point is the closest one
            print("You are closest to point " + str(x))
            broken = True
    step2 += 1
    for y in points:  #Same thing except it takes a step FORWARD
        if y == step2:
            print("You are closest to point " + str(y))
            broken = True
    if broken == True:  #If reached point, break loop
        break

# Normally you make the computer repeat this task AGAIN AND AGAIN until it reaches a certain point.
# So the more you know