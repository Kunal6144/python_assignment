length_of_fish = float(
    input('Enter the Length of Zander you have caught in centimeters: '))

if length_of_fish >= 42:
    print('Congrats you can caugth Zander that meets the size requirement!')
else:
    print(f'Sorry you will have to release the Zander fish back into the lake as it does not meet the criteria.')
    print(
        f'The Zander fish is short by {42 - length_of_fish}cm from meeting the criteria')
