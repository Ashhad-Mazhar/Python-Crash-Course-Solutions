favorite_numbers = {
    'Ashhad': [10, 7],
    'Butcher': [7],
    'Sherlock': [8, 6, 3],
    'Homelander': [2, 5, 7, 12, 312],
    'Bruce': [3, 4, 12, 3],
}

for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")