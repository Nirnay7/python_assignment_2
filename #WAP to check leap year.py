#WAP to check leap year
year = int(input('Enter year'))
if year%400 == 0:
    print('It is a leap year')
elif year%4 ==0:
    print('It is a leap year')
elif year%100 == 0:
    print('Is a not a leap year')
else:
    print('Not a leap year')