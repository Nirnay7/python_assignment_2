num = int(input("Enter a Number :"))   #12345
smallest= num
while (num > 0):                #num=0
    remainder=num%10            #remainder = 1
    if smallest>remainder:      # 12345 > 1
        smallest = remainder    # smallest = 1
    num //= 10                  # num = 0
print("The Smallest Digit is :", smallest)
