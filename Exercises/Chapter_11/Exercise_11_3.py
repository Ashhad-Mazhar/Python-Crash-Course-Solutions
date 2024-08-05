class Employee:
    """Class representing an employee"""
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, raise_amount:int=5000):
        self.salary += raise_amount