import random

choices = ["kivi", "käärid", "paber"]

player_wins = 0
computer_wins = 0

while player_wins < 3 and computer_wins < 3:
    player_choice = input("Valige kivi, käärid või paber: ").lower()
    computer_choice = random.choice(choices)

    print("Te valisite:", player_choice)
    print("Arvuti valis:", computer_choice)

    if player_choice == computer_choice:
        print("Mitte keegi võttis!")
    elif player_choice == "kivi" and computer_choice == "käärid":
        print("Te võitsite!")
        player_wins += 1
    elif player_choice == "käärid" and computer_choice == "paber":
        print("Te võitsite!")
        player_wins += 1
    elif player_choice == "paber" and computer_choice == "kivi":
        print("Te võitsite!")
        player_wins += 1
    else:
        print("Arvuti võitis!")
        computer_wins += 1

    print("Kogus: Teie {} - {} Arvuti".format(player_wins, computer_wins))

if player_wins > computer_wins:
    print("Te võitsite!")
else:
    print("Arvuti võitis!")