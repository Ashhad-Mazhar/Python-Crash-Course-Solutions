bruce_info = {
    'first_name': 'Bruce',
    'last_name' : 'Wayne',
    'age': 34,
    'city': 'Gotham',
}

butcher_info = {
    'first_name': 'Billy',
    'last_name': 'Butcher',
    'age': 50,
    'city': 'Chicago'
}

people = []
people.append(bruce_info)
people.append(butcher_info)

for person in people:
    for key, value in person.items():
        print(
            f"{person['first_name']}'s {key.replace('_',' ').title()} is {value}"
        )