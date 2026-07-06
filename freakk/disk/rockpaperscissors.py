import random

choice = ('r', 'p', 's')

while True:
    user_choice = input('rock paper or scissors (r/p/s): ').lower()

    if user_choice not in choice:
        print('Invalid choice')
        continue

    computer_choice = random.choice(choice)

    print(f'You chose {user_choice}')
    print(f'Computer chose {computer_choice}')

    if user_choice == computer_choice:
        print('Tie')
    elif user_choice == 'r' and computer_choice == 'p':
        print('You lost')
    elif user_choice == 'p' and computer_choice == 'r':
        print('You won')
    elif user_choice == 's' and computer_choice == 'r':
        print('You lost')
    elif user_choice == 'r' and computer_choice == 's':
        print('You won')
    elif user_choice == 'p' and computer_choice == 's':
        print('You lost')
    elif user_choice == 's' and computer_choice == 'p':
        print('You won')

    break