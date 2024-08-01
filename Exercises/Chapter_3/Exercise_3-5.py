guests = ['Butcher', 'Homelander', 'Soldier Boy']

print(f'You are invited to the dinner, {guests[0]}')
print(f'You are invited to the dinner, {guests[1]}')
print(f'You are invited to the dinner, {guests[2]}')

missing_guest = 'Homelander'

print(f'{missing_guest} cannot make it to the dinner.')

new_guest = 'Black Noir'

guests.remove(missing_guest)
guests.append(new_guest)

print(f'You are invited to the dinner, {guests[0]}')
print(f'You are invited to the dinner, {guests[1]}')
print(f'You are invited to the dinner, {guests[2]}')