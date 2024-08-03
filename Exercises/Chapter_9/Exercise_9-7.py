class User:
    """Represents a user"""

    def __init__(
            self, first_name: str, last_name: str,
            email_address: str, country: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.country = country
        self.login_attempts = 0

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
    
    def increment_login_attempts(self) -> None:
        self.login_attempts += 1
    
    def reset_login_attempts(self) -> None:
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name: str, last_name: str,
            email_address: str, country: str):
        super().__init__(first_name, last_name, email_address, country)
        self.privileges = [
            'can add a user',
            'can ban a user',
            'can delete a post'
        ]

    def show_privileges(self) -> None:
        for privilege in self.privileges:
            print(privilege)


admin = Admin('Ashhad', 'Mazhar', 'abc.com', 'Pakistan')
admin.show_privileges()