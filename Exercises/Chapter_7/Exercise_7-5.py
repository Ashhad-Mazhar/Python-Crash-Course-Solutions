while True:
    age = int(input('Enter your age: '))

    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    elif age > 12:
        cost = 15
    
    print(f'The cost of the ticket is ${cost}.')