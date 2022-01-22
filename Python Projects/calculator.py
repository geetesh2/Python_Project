def add(a,b):
    return int(a)+int(b)

def multiply(a,b):
    return int(a)*int(b)

def divide(a,b):
    return int(a)/int(b)

def subtract(a,b):
    return int(a)-int(b)

def power(a,b):
    return int(a)**int(b)

while(1):
    x = input("What operation you need to do \n press 1 to add \n 2 to multiply \n 3 to divide \n 4 to subract \n 5 to power \n q to quit \n")
    if(x=='q'):
        print("Thanks for using \n")
        break
    print("Give the values to calculate")
    a = input("First no. :- ")
    b = input("Second no. :- ")
    if(x=='1'):
        print(add(a,b))
    elif(x=='2'):
        print(multiply(a,b))
    elif(x=='3'):
        print(divide(a,b))
    elif(x=='4'):
        print(subtract(a,b))
    elif(x=='5'):
        print(power(a,b))
