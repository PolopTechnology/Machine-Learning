import numpy #Import

y_times = [] # List containing all y times

def linear(array1, mean, num): # function that has a data point as it's argument.
    dsec1 = array1[num] # then it checks how far away that data point is from the middle point.
    dsec2 = array1[num] 

    times = 0.0
    t = 0
    sec_times = 0.0
    s = 0
    global y_times
    while True:
       if dsec1 == mean[num]:
           print(t)
           if num == 1:
               y_times.append(times)
           break
       elif dsec2 == mean[num]:
           print(s)
           if num == 1:
               y_times.append(sec_times)
           break

       dsec1 -= 1
       times += 0.1
       t += 1
       dsec2 += 1
       sec_times += 0.1
       s += 1


d1 = [1,2]
d2 = [2,4]  # All data points
d3 = [5,3]
d4 = [4,4]
d5 = [5,5]

x = [1, 2, 3, 4, 5] # check points in x
y = [2, 3, 4, 5, 6] # check points in y

mean1 = numpy.median(x) # assigns middle point of x and y check points
mean2 = numpy.median(y)

means = [mean1, mean2] # SMASHING ALL MIDDLE POINTS

linear(d1, means, 0) #Function calls.
linear(d1, means, 1)
print("---")
linear(d2, means, 0)
linear(d2, means, 1)
print("---")
linear(d3, means, 0)
linear(d3, means, 1)
print("---")
linear(d4, means, 0)
linear(d4, means, 1)
print("---")
linear(d5, means, 0)
linear(d5, means, 1)

val = sum(y_times) # Sums up all y's

minus = val * mean1 # Multiplies y sum with middle point of x

final = mean2 - minus # THE FINAL CALCULATION
print("Start regression line at " + str(final) + " for less loss.") # The moment of truth

# %%%SIMULATION COMPLETE%%% #



    

