Compound Interest
p=int(input("Enter principle"))
t=int(input("enter time"))
r=int(input("Enter time"))
A=p*(1+r/100)**t
CI=A-p
print(round(CI,2))
