class User:
    def __init__(
            self, first_name: str, last_name: str,
            email_address: str, country: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.country = country

    def describe_user(self) -> None:
        """Prints a description of the user"""
        print("Here is a summary of the user's info:")
        print(f'\tFirst Name: {self.first_name}')
        print(f'\tLast Name: {self.last_name}')
        print(f'\tEmail Address: {self.email_address}')
        print(f'\tCountry: {self.country}')
    
    def greet_user(self) -> None:
        """Prints a personalized greeting to the user"""
        print(f'Hello, {self.first_name}')

user_1 = User('Ashhad', 'Mazhar', 'abc@gmail.com', 'Pakistan')
user_2 = User('Billy', 'Butcher', 'cunt@gmail.com', 'America')

user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()