import json

try:
    with open('number.json') as json_file:
        json_number = json_file.read()
        number = json.loads(json_number)
except FileNotFoundError:
    print('File not found')
else:
    print(f'{number} is your favorite number')