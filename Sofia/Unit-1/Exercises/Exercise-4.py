import random

def main():
    randomNumber = random.randint(0, 100)

    if(randomNumber >= 20):
        favourite = "dogs"
    elif(randomNumber >= 10):
        favourite = "cats"
    else:
        favourite = "bats"


    print("I love " + favourite) 


main()