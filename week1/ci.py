p=int(input("Enter principle"))
t=int(input())
r=int(input())
A=p*(1+r/100)**t
CI=A-p
print(round(CI,2))
