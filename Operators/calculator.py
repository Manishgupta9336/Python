a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
op = input("Choose a operator '+ - * / ' ")

if(op=="+"):
    print("Add- ",a+b)

if(op=="-"):
    print("Sub- ",a+b)

if(op=="*"):
    print("Mul- ",a*b)

if(op=="/"):
    if(b>0 or b<0):
        print("div- ",a/b)
    if(b==0):
        print("Invalid!!")
else:
    print("--Please Choose a correct operator-- ")

