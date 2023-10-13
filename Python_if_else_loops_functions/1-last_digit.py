import random
number = random.randint(-10000, 10000)
print(number)
num = 0
if number < 0:
    num = -number % 10
    
elif number > 0:
    num = number % 10
    
elif num > 5:
    print("the last digit of ", number, " is ", num, "and is greater than 5")
    
if num == 0:
    print("the last digit of ", number, " is ", num, "and is 0")
    
else :
    print("the last digit of ", number, " is ", num, "and is less than 6 and not 0")
    