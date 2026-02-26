p = int(input("Enter principal: "))
r = float(input("Enter rate: "))
t = int(input("Enter time: "))
a = p*(1+r/100)**t

ci = a-p

print(ci)
