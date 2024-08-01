guests = ['Butcher', 'Homelander', 'Soldier Boy']

print(f'You are invited to the dinner, {guests[0]}')
print(f'You are invited to the dinner, {guests[1]}')
print(f'You are invited to the dinner, {guests[2]}')

print("We found a bigger table")

guests.insert(0, 'Black Noir')
guests.insert(2, 'MM')
guests.append('Frenchie')

print(f'You are invited to the dinner, {guests[0]}')
print(f'You are invited to the dinner, {guests[1]}')
print(f'You are invited to the dinner, {guests[2]}')
print(f'You are invited to the dinner, {guests[3]}')
print(f'You are invited to the dinner, {guests[4]}')
print(f'You are invited to the dinner, {guests[5]}')

print("We can only invite two people for dinner")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f'We cannot accomodate you, {removed_guest}')

del guests[1]
del guests[0]

print(guests)