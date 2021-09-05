#WAP to calculate factorial of any number 
i = 1
fact = 1
n = int(input('Enter a number'))
if n<0:
    print("Factorial doesn't exist for negative number")
elif n==0 or n==1:
    print("Factorial of", n ,'is 1')
else:
    for i in range(1,n+1): #i = 5
        fact = fact*i  #fact=120
    print('Factorial of', n, 'is', fact)