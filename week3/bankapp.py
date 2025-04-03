def credit(bal,val):
    bal+=val
    return bal
def debit(bal,val):
    bal-=val
    return bal
def checkbalance(bal):
    print("check balance:",bal)
bal=0
bal=credit(bal,2000)
checkbalance(bal)
print("amount credited:",bal)
bal=debit(bal,1400)
print("amount debited:",bal)
checkbalance(bal)
print(bal)
