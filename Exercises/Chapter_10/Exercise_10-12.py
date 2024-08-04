import json

try:
    with open('number.json') as json_file:
        json_number = json_file.read()
        number = json.loads(json_number)
except FileNotFoundError:
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Please enter a valid number')
        else:
            break

    with open('number.json', 'w') as json_file:
        json_string = json.dumps(number)
        json_file.write(json_string)
else:
    print(f'{number} is your favorite number')