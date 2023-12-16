def game():
    U1 = str(input("enter rock, paper & scissor:"))
    U2 = str(input("enter rock, paper & scissor:"))
    
    if U1 == U2:
        print("tie")
    elif U1 == "rock":
        if U2 == "paper":
            print("User 2 wins")
        else:
            print("User 1 wins")
    elif U1 == "paper":
        if U2 == "scissor":
            print("User 2 wins")
        else:
            print("User 1 wins")
    elif U1 == "scissor":
        if U2 == "rock":
            print("User 2 wins")
        else:
            print("User 1 wins")
    
    ch = input("do you want to play again? (y/n): ")
    if ch == 'y':
        game()
    else:
        print("thanks for playing")

# Call the game function to start the game
game()
