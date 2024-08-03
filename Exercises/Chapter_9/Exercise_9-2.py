class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) -> None:
        print(f'Restaurant Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}')

    def open_restaurant(self) -> None:
        print(f'{self.restaurant_name} is now open.')


restaurant_1 = Restaurant('Ranchers', 'Fast Food')
restaurant_2 = Restaurant('Ahmed Burger', 'Fast Food')
restaurant_3 = Restaurant('Butt Karahi', 'Continental')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()