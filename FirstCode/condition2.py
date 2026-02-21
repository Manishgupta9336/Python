age = int(input("Enter age: "))
if age<18:
    print("Minor")
elif age>=18 and age<=35:
    print("Young Adult")
else:
    print("Adult")