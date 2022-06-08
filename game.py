# Simple game of rock paper scissors
from secrets import choice


print('\nWelcome to our game of Rock Paper Scissors\n')
game_on = True

# computer randomly makes choice between rock paper scissors and returns choice
def Picks_Randomly():
    import random
    items = ['R', 'P', 'S']
    computer_choice = random.choice(items)
    print('computer choice is '+computer_choice)
    return computer_choice

# ensures human player picks among choice presented
def Verify_Choice(player_pick):
    my_choice = True
    while(my_choice):
        if (player_pick != 'R' and player_pick != 'S' and player_pick != 'P'):
            print('Invalid choice. Please try again')
            player_pick = input('What is your choice: ')
            player_pick = player_pick.upper()
        else:
            print('player pick is '+player_pick)
            my_choice = False
            return player_pick

#conditions for a draw game
def Draw_Game_Checker(player_choice, computer_choice):
    if(player_choice == 'R' and computer_choice == 'R'):
        return (print("Draw game"))
    if(player_choice == 'P' and computer_choice == 'P'):
        return (print("Draw game"))
    if(player_choice == 'S' and computer_choice == 'S'):
        return (print("Draw game"))

#Conditions for user to win game
def Player_To_Win(player_choice, computer_choice):
    if(player_choice == 'R' and computer_choice == 'S'):
        return(print("You WIN!"))
    elif(player_choice == 'P' and computer_choice == 'R'):
        return(print("You WIN!"))
    elif(player_choice == 'S' and computer_choice == 'P'):
        return(print("You WIN!"))
    #elif(Draw_Game_Checker(player_choice, computer_choice)):
    #    print("Draw Game")
    #else:
    #    print("Computer Wins!")

#Conditions for computer to win game
def Computer_To_Win(player_choice, computer_choice):
    if(player_choice == 'S' and computer_choice == 'R'):
        return(print("You LOSE!"))
    elif(player_choice == 'R' and computer_choice == 'P'):
        return(print("You LOSE!"))
    elif(player_choice == 'P' and computer_choice == 'S'):
        return(print("You LOSE!"))

while(game_on):
    print('Starting game')
    player_pick = input(
        "What is your pick\n'R' for Rock\n'P' for Paper\n'S' for Scissors\nChoose one: ")
    player_pick = player_pick.upper()
    Verify_Choice(player_pick)
    computer_pick = Picks_Randomly()
    #winning conditions call
    player_wins = Player_To_Win(player_pick, computer_pick)
    computer_wins = Computer_To_Win(player_pick, computer_pick)
    draw_game = Draw_Game_Checker(player_pick, computer_pick)

    #checks for overall winner 
    if(player_wins):
        print(player_wins)
    elif(computer_wins):
        print(computer_wins)
    elif(draw_game):
        print(draw_game)

    #Ask user whether like to perform another operation
    player_continue = input("Would you like to try again?\nYes[y] or No[n]: ")
  
    if player_continue.lower() == "y":
        continue
    #If yes, restart loop else break loop
    if player_continue.lower() == "n":
        game_on = False
        print("Thanks for playing our ROCK PAPER SCISSORS game. BYE!")
    

    

    
