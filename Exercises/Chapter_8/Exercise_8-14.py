def make_car(manufacturer: str, model_name: str, **car_profile):
    car_profile['manufacturer'] = manufacturer
    car_profile['model_name'] = model_name
    return car_profile

my_car = make_car('Honda', 'Civic', color='Black', tow_package=True)

print(my_car)