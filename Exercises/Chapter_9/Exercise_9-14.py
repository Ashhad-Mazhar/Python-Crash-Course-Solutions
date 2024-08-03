import random

new_list = [
    'a', 'b', 'c', 'd', 'e', 'f','g',
    'h', 'i', 'j', 1, 2, 3, 4, 5
]

sequence = []
for i in range(0, 4):
    sequence.append(str(random.choice(new_list)))

print(f'{sequence} wins the lottery.')