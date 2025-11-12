print("Welcome to Rock-Paper-Scissors !")
choice = str(input("Choose rock, paper, or scissors: "))
while  choice.lower() != 'paper' or choice.lower() !='rock' or choice !='scissors':
    print("Invalid choice, choose again")
    choice = str(input("Choose rock, paper, or scissors: "))

print(f"You chose: {choice}")