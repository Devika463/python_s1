class BankAccount:
  def __init__(self, account_number, name, account_type, balance=0.0):
    self.account_number = account_number
    self.name = name
    self.account_type = account_type
    self.balance = balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive.")
    self.balance += amount
    print(f"Deposited ${amount:.2f} into account {self.account_number}.")

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdrawal amount must be positive.")
    if amount > self.balance:
      raise InsufficientFundsError(f"Insufficient funds in account {self.account_number}.")
    self.balance -= amount
    print(f"Withdrew ${amount:.2f} from account {self.account_number}.")

class InsufficientFundsError(Exception):
  pass
account1 = BankAccount("123456", "John Doe", "Savings", 10000.00)
account1.deposit(500.00)  # Deposit $500
account1.withdraw(200.00)  # Withdraw $200 (successful)
try:
    account1.withdraw(1500.00)  # Attempt to withdraw more than balance (raises InsufficientFundsError)
except InsufficientFundsError as e:
    print(e)
