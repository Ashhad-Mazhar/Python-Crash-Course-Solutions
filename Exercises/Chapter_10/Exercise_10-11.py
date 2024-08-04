import json

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