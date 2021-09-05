#WAP to display exact pattern as below using zip() 
'''
1   5
2   4
3   3
4   2
5   1
'''
num = [ "1", "2", "3", "4", "5" ]
reverse_num = ["5","4","3","2","1"]
for n, r_n in zip(num,reverse_num):
    print ( "%s   %s" %(n, r_n))