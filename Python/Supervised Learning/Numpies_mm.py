#%%BREAST CANCER CLASSIFICATION SYSTEM%%

print("Age?")  #ACCEPTS INPUT FROM USER AS TO THE AGE AND SIZE OF THE TUMOR.
age = float(input())
print("Tumor Size?")
size = float(input())

#VARIABLES
q = age + size #TAKES THE USER'S INPUTS AND SUMS THEM
i = 7.0 # HOW MANY TIMES THE WHILE LOOP MUST LOOP
j = 0 
l = 0  
g = q
h = q

if q > 6.9:
    print("Your tumor has been identified as malignant.")
elif q < 6.0:
    print("Your tumor is benign")

elif not q < 6.0: #THIS IS THE CLASSIFICATION SYSTEM.
    while i > g: #these loops ADDS 0.1 for each loop.
        g += 0.1
        j += 0.1
    close_to_mal = j
    i = 5.9
    while i < h:
        h -= 0.1
        l += 0.1
    close_to_beg = l

    if close_to_beg > close_to_mal:   #These if statements compare the two variables to see which on is farthest
        print("Your tumor is closer to malign") #benign. If your input is farther from benign than malign it will
    elif close_to_beg < close_to_mal:  #classify the tumor as malign. if it is farther from malign than benign,
        print("Your tumor is closer to benign") #THEN it will classify as benign.


print("ATTENTION: This is purely for educational purposes. If you DO have a tumor, visit a hospital.")
#yeah exactly ^
