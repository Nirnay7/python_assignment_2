#WAP to find palindrome number
n=int(input("Enter number:"))     #2002
temp_num = n
rev=0
while(temp_num >0):       #temp_num = 0
    dig=temp_num %10      #dig = 2
    rev=rev*10+dig        #rev = 200*10+2= 2002
    temp_num //=10        # temp_num  = 0
if(n==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")