n = int(input("enter a number:- "))
l = len(str(n))
c = n
sum = 0

while(n>0):
    r = n%10
    sum = sum + (r**l)
    n = n//10
if (sum==c):
    print("Yes it is Armstrong number ")
else:
    print("Not a Armstrong")