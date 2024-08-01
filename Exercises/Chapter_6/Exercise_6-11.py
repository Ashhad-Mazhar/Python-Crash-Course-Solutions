cities = {
    'lahore': {
        'country': 'pakistan',
        'fact': 'lahore lahore ae',
    },
    'gotham': {
        'country': 'gotham',
        'fact': 'I (batman) live here',
    },
    'gujranwala': {
        'country': 'pakistan',
        'fact': 'cannot think of anything'
    }
}

for city, city_info in cities.items():
    print(f'{city.title()}:')
    for key, value in city_info.items():
        print(f"\t{city.title()}'s {key} is {value}.")