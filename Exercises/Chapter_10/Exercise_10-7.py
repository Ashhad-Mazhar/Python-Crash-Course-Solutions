while True:
    try:
        number_1 = int(input('Enter a number: '))
        number_2 = int(input('Enter another number: '))
    except ValueError:
        print(f'Please enter only numbers')
    except KeyboardInterrupt:
        print('\n\nThanks for using the program')
        break
    else:
        sum = number_1 + number_2
        print(sum)