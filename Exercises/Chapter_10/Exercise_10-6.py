try:
    number_1 = int(input('Enter a number: '))
    number_2 = int(input('Enter another number: '))
except ValueError:
    print(f'Please enter only numbers')
else:
    sum = number_1 + number_2
    print(sum)