a = input("First String: ")
b = input("Second String: ")

s1 = list(a)
s2 = list(b)
s1.sort()
s2.sort()

if(s1==s2):
    print("Yes")
else:
    print("No!")