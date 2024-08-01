numbers = [x**3 for x in range(1, 11)]

for number in numbers:
    print(number)

print(f"The first three values in the list are: {numbers[:3]}")

print(f"Three items from the middle of the list are: {numbers[3:6]}")

print(f"The last three items in the list are: {numbers[-3:]}")