import random

def play():
    while True:
        user = input('''
                           r for rock 
                           p for paper
                           s for scissor
    
    
    enter your input here  :   ''')
        if user.lower()=="r":
            print("your choice is ROCK")
        elif user.lower()=="p":
            print("your choice is PAPER")
        elif user.lower() == "s":
            print("your choice is SCISSOR")
        else :
            print("please enter the valid option")

        computer = random.choice(["r","p","s"])

        if user in ["r","p","s"]:
            if computer == "r":
                print("computer's is ROCK")
            elif user.lower() == "p":
                print("computer's choice is PAPER")
            elif computer == "s":
                print("computer's choice is SCISSOR")

            if computer == user.lower():
                print("    YOU WON THE GAME             ")
            else:
                print("    COMPUTER WON THE GAME  ")




play()
