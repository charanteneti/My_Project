import sys
class Bank:
	bankname="Kiran Bank"
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance

	def deposit(self,amt):
		self.balance=self.balance+amt
		print(amt,"deposited"," Total amount: ",self.balance)

	def withdraw(self,amt):
		if amt>self.balance:
			print("insufficient balance: ", amt)
			sys.exit()
		self.balance=self.balance-amt
		print(amt," deducted from account ", " the remaining balance is: ", self.balance)
print("Welcome: ",Bank.bankname)
name=input("Enter name ")
c=Bank(name)
while True:
	print("select option: Deposit-D/d or Withdraw: W/w or Exit E/e :")
	option=input("Select Option: D/W ")
	
	if option=='D':
		amt=int(input("enter amount: "))
		c.deposit(amt)
	
	elif option=='E':
		print("Thank You:")
		sys.exit()
	else:
		print("invalid Option")
