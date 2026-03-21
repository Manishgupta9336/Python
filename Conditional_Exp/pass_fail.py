m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

percentage = (m1+m2+m3)/3

if(percentage>40):
    print("---Pass---")
else:
    print("---Fail---")