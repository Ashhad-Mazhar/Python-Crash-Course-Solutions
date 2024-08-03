def Build_Profile(first_name: str, last_name: str, **user_profile):
    """
    Builds a dictionary to represent a user profile
    based on the info the user provides
    """

    user_profile['first_name'] = first_name
    user_profile['last_name'] = last_name

    return user_profile

my_profile = Build_Profile(
    'Ashhad', 'Mazhar', city='Lahore',
    country='Pakistan', university='UET'
)

for key, value in my_profile.items():
    print(f'{key}: {value}')