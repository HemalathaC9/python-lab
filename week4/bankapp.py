def credit(bal,transactions):
       amount=int(input("enter amount to credit"))
       bal-=amount
       transactions.append(amount)
       print("credited amount:",amount)
       return bal,transactions
def debit(bal,transactions):
        amount=int(input("enteramount to debit:"))
        if amount<bal:
           bal-=amount
           transactions.append(-amount)
           print("debited amount",amount)
           return bal,transactions
        else:
             print("invalid")
def check_balance():
        print("current balance",bal)
def last_5_transactions(transactions):
        for transaction in transactions:
            print(transaction)
bal=0
transactions=[]
while True:
    print("bank applications")
    print("1.credited\n2.debited\n3.check balance\n4.last 5 transactions\n5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
       bal,tran=credit(bal,transactions)
    elif choice==2:
         bal,tran=debit(bal,transactions)
    elif choice==3:
         check_balance(bal)
    elif choice==4:
         last_5_transactions(transactions)
    elif choice==5:
        print("thankyou....")
        break
    else:
        print("wrong choices")
             
        
    
