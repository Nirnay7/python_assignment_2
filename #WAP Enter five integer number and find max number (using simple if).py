#WAP Enter five integer number and find max number (using simple if)
num = int(input("Enter a Number :"))
Largest=0
while (num > 0):             #num=0
    remainder=num%10         #remainder = 1
    if Largest<remainder:    #5<5
        Largest = remainder  # largest = 5
    num //= 10               # num = 0
print("The Largest Digit is :", Largest)