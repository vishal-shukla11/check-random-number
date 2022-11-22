#this is project about the random and using def function

import random
def check_number(num1,num2):
    rand=random.randint(num1,num2)
    print("The random number from given range is:",rand)
    if rand>=0:
        print(rand,"is positive number.")
    else:
        print(rand,"is negative number.")
    if rand % 2 == 0:
        print(rand,"is even.")
    else:
        print(rand,"is odd.")

    if rand > 1 or rand<0:
        # check for factors
        for i in range(2, abs(rand)):
            if (rand % i) == 0:
                print(rand, "is composite number.")
                print(i, "times", rand// i, "is", rand)
                break
        else:
            print(rand, "is a prime number")
    elif rand == 0 or 1:
            print(rand, "is a neither prime NOR composite number")
num1=int(input("enter the starting range: "))
num2=int(input("enter the end range: "))
check_number(num1,num2)


