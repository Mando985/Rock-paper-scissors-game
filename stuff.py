def playagain():
    h = input("Do you want to play again? (Y/N)\n==>")
    j = h.lower()
    if j == "y":
        game()
    else:
        pass


def game():
    import random
    l1 = ["rock", "paper", "scissors"]
    a, b, c = l1
    y = random.choice(l1)
    str1 = input("Choose any one of the given option (type the option only):\nA) Rock\nB) Paper\nC) Scissors\n==> ")
    x = str1.lower()
    options = ["a", "b", "c"]
    if x not in options:
        print('Please enter a given option')
        game()
    if x == "a":
        if y == a:
            print("you both chose rock, try again")
            game()
        elif y == b:
            print("you lose, the computer chose paper")
            playagain()
        elif y == c:
            print("you win! the computer unfortunately chose scissors")
            playagain()
    elif x == "b":
        if y == a:
            print("you win! the computer unfortunately chose rock")
            playagain()
        elif y == b:
            print("you both chose paper, try again")
            game()
        elif y == c:
            print("you lose, the computer chose scissors")
            playagain()
    elif x == "c":
        if y == a:
            print("you lose, the computer chose rock")
            playagain()
        elif y == b:
            print("you win! the computer unfortunately chose paper")
            playagain()
        elif y == c:
            print("you both chose scissors, try again")
            game()


game()
