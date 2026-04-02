def largest(a,b,c):
    if(a>b and a>c):
        return f"a is greater: {a}"
    elif(b>a and b>c):
        return f"b is greater: {b}"
    else:
        return f"c is greater: {c}"
    
print(largest(89,677,820))