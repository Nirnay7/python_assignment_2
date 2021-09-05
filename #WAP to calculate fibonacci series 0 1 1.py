#WAP to calculate fibonacci series 0 1 1 2 3 5 8 13
n = int(input('Enter a number'))
f0 = 0
f1 = 1
i = 0
fn = 0
if n<0:
    print('Negative numbers are not allowed')
elif n==0:
    print('Fibonacci series of 0 is 0')
else:
    for i in range(1, n): 
        fn = f0 + f1
        f0 = f1
        f1 = fn
        print(f1)
    print('Fibonacci series of', n, 'is',f1 )