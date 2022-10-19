def game():
    import random
    l1 = ["rock", "paper", "scissors"]
    a, b, c = l1
    y = random.choice(l1)
    str1 = input("Choose any one of the given option (type the option only):\nA) Rock\nB) Paper\nC) Scissors\n==> ")
    x = str1.lower()
    options = ["a", "b", "c"]
    if x in options:
        if x == "a":
         if y == a:
            print("you both chose rock, try again")
            game()
         elif y == b:
            print("you lose, the computer chose paper")
         elif y == c:
            print("you win! the computer unfortunately chose scissors")
        elif x == "b":
           if y == a:
            print("you win! the computer unfortunately chose rock")
           elif y == b:
            print("you both chose paper, try again")
            game()
           elif y == c:
            print("you lose, the computer chose scissors")
        elif x == "c":
           if y == a:
            print("you lose, the computer chose rock")
           elif y == b:
            print("you win! the computer unfortunately chose paper")
           elif y == c:
            print("you both chose scissors, try again")
            game()
        h = input("Do you want to play again? (Y/N)\n==>")
        j = h.lower()
        if j == "y":
           game()    
    else:
        print("Invalid input, try again")
        game()       


game()     
