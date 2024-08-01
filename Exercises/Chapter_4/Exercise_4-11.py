pizzas = ['Fajita Pizza', 'Lasagna Pizza', 'Supreme Pizza']

for pizza in pizzas:
    print(f"I like {pizza}")
print("This is a message outside the for loop")

friend_pizzas = pizzas[:]

pizzas.append('Cheesy Pizza')
friend_pizzas.append('Malai Boti Pizza')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")