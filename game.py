import random
active = True

while active:

    computer_num = random.randrange(1,11)
    win = False
    prompt = "\nI'm thinking of a number between 1 and 10. Guess which number: "

    for i in range(3):
        user_num = int(input(prompt))

        if user_num == computer_num:
            win = True
            break

        prompt = "That wasn't right. Try again: "

    if win == True:
        print(f"\nGreat Job! {computer_num} is the number I was thinking.")
    else:
        print(f"\nBetter luck next time. The number I was thinking was {computer_num}.")


    play = input("Do you want to play again (Y/n): ")
    if play == 'Y' or play == 'y':
        continue
    elif play == 'N' or play == 'n':
        active = False


