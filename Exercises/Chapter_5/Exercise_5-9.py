usernames = []

if not usernames:
    print('We need to find some users.')

for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, thanks for logging in')