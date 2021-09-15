from random import randint
print("...Rock.....")
print("...Paper.....")
print("...Scissors.....")

player =input("player make your moves..\n")
random_Number = randint(0,2)

if random_Number == 0:
    computer = "rock"
elif random_Number == 1:
    computer = "scissors"
else:
    computer = "paper"
print(f"computer plays {computer}\n")

if player == computer:
    print("Its a tie")
elif player == "rock":
    if computer == "paper":
        print("Paper wins")
    else:
        print("rock wins")
elif  player == "paper":
    if computer ==   "rock":
        print("paper wins")
    else:
        print("Scissors Wins")   
elif player == "scissors" :
    if computer == "rock":
        print("Rocks wins")
    else:
        print("scissors wins")    
else:
    print("something went wrong!!!") 


                                 