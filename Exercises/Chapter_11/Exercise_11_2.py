def return_city_country(city: str, country: str, population:int=''):
    if population:
        result = f'{city.title()}, {country.title()} - population {population}'
    else:
        result = f'{city.title()}, {country.title()}'
    return result