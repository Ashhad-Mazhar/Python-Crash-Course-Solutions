favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_vote = ['jen', 'ashhad', 'sarah', 'john']

for person in people_to_vote:
    if person in favorite_languages.keys():
        print(f'Thank you for taking the poll, {person}')
    else:
        print(f'Please take the poll, {person}')