# Make a two-player Rock-Paper-Scissors game.

player1 = input("Choose Rock-Paper-Scissors: ")
player2 = input("Choose Rock-Paper-Scissors: ")
while player1 == 'rock':
    if player2 == 'rock':
        print("PLAY Again!")
        break
    elif player2 == 'paper':
        print("player 2 wins!")
        break
    elif player2 == 'scissors':
        print("player 1 wins!")
        break
while player1 == 'paper':
    if player2 == 'rock':
        print("player 1 wins!")
        break
    elif player2 == 'paper':
        print("PLAY Again!")
        break
    elif player2 == 'scissors':
        print("player 2 wins!")
        break
while player1 == 'scissors':
    if player2 == 'rock':
        print("player 2 wins!")
        break
    elif player2 == 'paper':
        print("player 1 wins!")
        break
    elif player2 == 'scissors':
        print("PLAY Again!")
        break
