dream_vacations = dict()

while True:

    user_input = input('Where would you go for your dream vacation? ')

    if user_input == 'quit':
        break

    if user_input in dream_vacations:
        dream_vacations[user_input] += 1
    else:
        dream_vacations[user_input] = 1

print('The poll results are as follows:')
for place, votes in dream_vacations.items():
    print(f'\t{place}: {votes}')