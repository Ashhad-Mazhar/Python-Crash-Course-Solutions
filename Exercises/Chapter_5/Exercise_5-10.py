current_users = ['admin', 'ashhad', 'soldier_boy', 'butcher', 'sherlock']
lower_case_current_users = [user.lower() for user in current_users]

new_users = ['ashhad', 'john', 'Butcher', 'greg', 'frenchie']

for user in new_users:
    if user.lower() in lower_case_current_users:
        print(f'Username {user} already in use')
    else:
        print(f'Username {user} is available')