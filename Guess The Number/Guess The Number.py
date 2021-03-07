import random

myNumber = random.randint(1 , 21)

print("-------------------------------------------------------------")
print("I am thinking of a number between 1 & 20.")
print("You'll have 5 chances to guess my number. TAKE A GUESS!")

for i in range(0, 5):
    guessNumber = int(input())

    if guessNumber == myNumber:
        print("You got it! I was thinking of" , myNumber)

    elif guessNumber < myNumber:
        print("Too Low")
        print("You have" , (4-i) , "chances left")

    elif guessNumber > myNumber and guessNumber < 21:
        print("Too High")
        print("You have" , (4-i) , "chances left")
    
    elif guessNumber > 21:
        print("BETWEEN 1 & 20...!")
        print("You have" , (4-i) , "chances left")

    else:
        break
