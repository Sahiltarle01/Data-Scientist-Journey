# For loop

for i in range(5):      # stop
    print(i)
    
for i in range(1,6):    # start, stop
    print(i)
    
for i in range(2,11,2): # start, stop, step
    print(i)

#Print numbers 1–10
for i in range(1,11):
    print(i)
    
#Print name 5 times
for i in range(5):
    print("Sahil")
    
#Print even numbers
for i in range(2,21,2):
    print(i)

#Print odd numbers
for i in range(1,20,2):
    print(i)
    
#Multiplication Table
number = int(input("Enter Number: "))
for i in range(1,11):
    print(number,"*",i,"=",number*i)
    
# Break
# The break keyword is used to break out from loop
for i in range(1,11):
    if i == 5:
        break
    print(i)
    
# Continue  
# Use the continue keyword to end the current iteration in a loop, but continue with the next.
for i in range(1,6):
    if i == 3:
        continue
    print(i)

# Pass
# It uses for do nothing in loop at a current time, but use for feature use.
for i in range(5):
    pass
print("Program Finished")

# Nested Loop
# Loop inside another loop.
for i in range(3):

    for j in range(3):

        print(i,j)