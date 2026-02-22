n = int(input("Enter a number:- "))
c = n
sum = 0

while(n>0):
    r = n%10
    sum = (sum*10) + r
    n = n//10
if (sum==c):
    print("Yes! palindrom ")
else:
    print("Not Palindrom")