year = int(input('Enter Year you want to check if it is leap year or not: '))

if year % 4 == 0 and year % 100 != 0:
    print('Its a Leap Year')
elif year % 400 == 0:
    print('Its a Leap Year')
else:
    print('Its not a Leap Year')
