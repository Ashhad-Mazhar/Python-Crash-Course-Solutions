class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self) -> None:
        print(f'Restaurant Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')

    def open_restaurant(self) -> None:
        print(f'{self.restaurant_name} is now open.')

    def set_number_served(self, new_number_served: int) -> None:
        self.number_served = new_number_served
    
    def increment_number_served(self, increment_value: int) -> None:
        self.number_served += increment_value


restaurant = Restaurant('Ranchers', 'Fast Food')

print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)
restaurant.set_number_served(34)
print(restaurant.number_served)
restaurant.increment_number_served(23)
print(restaurant.number_served)