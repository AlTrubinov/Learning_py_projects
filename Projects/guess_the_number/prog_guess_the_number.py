import random

def guess_game(max_range):
    number = random.randint(0, max_range)

    print(f'Please guess the number [0 - {max_range}]')
    guess = int(input())

    while guess != number:
        if guess > number:
            print('Try again with a smaller number')
        else:
            print('Try again with a bigger number')
        guess = int(input())

    else:
        print('Yeeeah, you guessed!!')
    pass

print('Do you wanna play?')
answer =input()

while answer not in ['No', 'N', 'n', 'no', '']:
    print("Let's play")
    print('Choose a range of numbers')
    r_number = int(input())
    while r_number < 1:
        print("Choose another number bigger than zero")
        r_number = int(input())
    guess_game(r_number)
    print('Do you wanna play again (Y/N)?')
    answer = input()
else:
    print('Ok')