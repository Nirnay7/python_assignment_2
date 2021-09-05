#WAP to check armstong number
num = int(input("Enter a number: "))
sum = 0
temp_num = num
while temp_num > 0:         #temp = 1
   digit = temp_num % 10    #digit = 1
   sum += digit ** 3        #sum= 152+1*1*1 = 153
   temp_num //= 10          #temp = 0
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
