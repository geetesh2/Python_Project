import numpy as np
x = np.random.randint(1,100)
Y=0
chances = 0 
while Y!=x:
    chances+=1
    Y = input("Guess the No.")
    if int(Y)==x:
        print("Congrats! Your guess was correct")
        print(f"And You took {chances} chances to guess the correct Number")
        break
    elif int(Y)>x:
        print("You guessed a Greater no.")
    else:
        print("You guessed a smaller no.")


