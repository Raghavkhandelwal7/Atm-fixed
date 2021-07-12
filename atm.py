class Atm():
    def __init__(self,atmCardNum,pinNum):
        self.atmCardNum=atmCardNum
        self.pinNum=pinNum
       

    def BankAtmCardNum(self):
        return self.atmCardNum

    def BankPinNum(self):
        return self.pinNum

    balance=1000000

    print("Welcome to the Atm!")
    print("Note: this is just for fun and the money you start with will always be 1,000,000")
    print("and that the balance will get reset eachtime you run this program again")
    print("and you cant withdraw money in decimals also enter the card and pin number in integers")

    AtmCardNumber=int(input("Please enter you Atm Card Number (12 digits please): "))
    AtmCardPin=int(input("Please enter you card pin  (4 digits please): "))

    print("the first input would be for withdrawl and the second would be for depositon also the third input would be for checking you balance")

    withdrawl=int(input("Withdraw you cash (Enter 0 if you dont want to withdraw any money): "))
    balance=balance-withdrawl

    if balance<withdrawl:
        print("insufficent funds try again or try adding more money into your account")

    deposition=int(input("Add money to your account (Enter 0 if you dont want to): "))
    balance=balance+deposition

    print("Your balance is: ", balance)
    print("Your card number: ", AtmCardNumber)
    print("Your card pin: ", AtmCardPin)

print("this is for the actual project so thats why there is extra stuff written here")
account1 = Atm('1034956781234','6734')
print(account1.BankAtmCardNum())
print(account1.BankPinNum())
    
