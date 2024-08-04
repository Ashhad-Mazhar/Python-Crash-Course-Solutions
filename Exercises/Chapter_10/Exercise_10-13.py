import json

user_info = dict()

username = input('What is your name? ')
print("IT DOESN'T MATTER WHAT YOUR NAME IS!\n\t\t- The Rock")
user_info['username'] = username

user_age = input('What is your age? ')
print("IT DOESN'T MATTER WHAT YOUR AGE IS!\n\t\t- The Rock")
user_info['user_age'] = user_age

user_country = input('What is your country? ')
print("IT DOESN'T MATTER WHAT YOUR COUNTRY IS!\n\t\t- The Rock")
user_info['user_country'] = user_country

json_contents = json.dumps(user_info)

with open('user_info.json', 'w') as json_file:
    json_file.write(json_contents)

with open('user_info.json') as json_file:
    json_contents_2 = json_file.read()
    user_info_2 = json.loads(json_contents)
print('The user info:')
for key, value in user_info_2.items():
    print(f'- {key}: {value}')