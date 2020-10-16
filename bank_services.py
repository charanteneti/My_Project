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
