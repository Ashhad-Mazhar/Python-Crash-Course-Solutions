pet_1 = {
    'kind': 'cat',
    'owner': 'selina'
}
pet_2 = {
    'kind': 'dog',
    'owner': 'butcher'
}
pet_3 = {
    'kind': 'hamster',
    'owner': 'hughie'
}

pets = []
pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)

for pet in pets:
    for key, value in pet.items():
        print(f"The pet's {key} is {value}.")