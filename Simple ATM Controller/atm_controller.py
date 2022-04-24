class Bank:
  # Bank should hold follwoing informations 
  # name, card_number, pin, account, balance 

  def __init__(self):
    self.bank_data = {}

  def add_information(self, name, card_num, pin, account, balance):
    # add input information to bank_data
    self.bank_data[card_num] = {"name" : name, "pin": pin, "account":{account:balance}}

  def add_account(self, card_num, account, balance):
    # if card number is valid => add the account
    if card_num in self.bank_data:
      self.bank_data[card_num]["account"][account] = balance

  def check_pin(self, card_num, input_pin):
    # if input_pin is valid => access to according account 
    if card_num in self.bank_data and self.bank_data[card_num]["pin"] == input_pin:
      return self.bank_data[card_num]["account"]
    # else None 
    else:
      return None

  
  def update_account(self, card_num, account, input_balance):
    # if card_num & account is valid => update input_balance 
    if self.bank_data[card_num]["account"][account] in self.bank_data[card_num]["account"]:
      self.bank_data[card_num]["account"] = input_balance
      return True
    else:
      return False

class Controller:
  # the Controller should be able to do follwoing actions:
  # insert card # check pin 
  # account select 
  # check balance, deposit, withdraw, # update after balance change 

  def __init__(self, bank, cash):
    self.Bank = bank
    self.accounts = None # to put the inserted cart account 
    self.cash_bin = cash

  def insert_card(self, card_num, pin):
    # after inserting card => must check pin number 
    self.accounts = self.Bank.check_pin(card_num, pin)
    if self.accounts is None:       # if invalid pin number => access denied
      return print(f"Invalid PIN, access denied. Please enter valid PIN")
    else:        # if valid pin number => welcome with personalized message
      return print(f"Welcome {self.Bank.bank_data[card_num]['name']}")

  def select_account(self, account):
    # checking if the selected account is in the card 
    if account in self.accounts:
      return True
    else:
      return False

  def account_actions(self, card_num, account, action, amount=0):
    # settin the default amount to zero as there are actions such as checking balance 
    # actions would be checkling balance, withdrawing, depositing
    if action == "Check Balance":       # returning account value 
      return self.accounts[account]
    elif action == "Withdraw":          # withdrawing the input_amount 
      if self.accounts[account] >= amount and self.cash_bin >= amount:      # when current balance is bigger than the input amount & cash_bin is bigger than amount 
        new_balance = self.accounts[account] - amount     # deduct the input_amount
        self.accounts[account] = new_balance              # update the account 
        self.Bank.update_account(card_num, account, new_balance)      # and the amount to the database 
        return print(f"Withdraw of {amount} has been processed. Current balance is {self.accounts[account]}")
      else:
        return print(f"Withdraw of {amount} is invalid. Current balance is {self.accounts[account]}")
    elif action == "Deposit":           # depositing the input_amount
      new_balance = self.accounts[account] + amount       # add the input amount to current account balance
      self.cash_bin += amount                             # add the amount to the cash_bin for the future process
      self.accounts[account] = new_balance                # update the added balance to the current account
      self.Bank.update_account(card_num, account, new_balance)          # and the amount to the database 
      return print(f"Deposit of {amount} has been processed. Current balance is {self.accounts[account]}")
    else: # for unavailable actions
      return print(f"Invalid action. Please enter a valid action.")
