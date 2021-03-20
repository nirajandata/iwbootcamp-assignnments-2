class Bank():
  def __init__(self, amount):
    self.money=amount
    print("hello to xyz Bank, your balance is ",self.money)
  
  def deposit(self,amount):
   self.money+=amount
   print("your balance is updated to ",self.money)
  
  def withdraw(self,amount):
    if self.money>=amount:
      self.money-=amount
      print("your new balance is ",self.money)
    else:
      print("you don't  have enough money")  

a=Bank(100)
a.deposit(50)
a.withdraw(100)