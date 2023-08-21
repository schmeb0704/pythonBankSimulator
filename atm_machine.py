class ATM:
  known_accounts = []
  accessed_account = None
  is_being_used = False
  def __init__(self, balance, address, account_list, parent_bank):
    self.balance = balance
    self.address = address
    self.known_accounts = [*account_list]
    self.parent_bank = parent_bank

  def insert_card(self, card_number):
    validated_account = self.validate_card(card_number)
    if validated_account != None:  
      print(f"Welcome, {validated_account.account_name}!")
      return self.validate_pin(validated_account)
    else:
      print(f"Card number not found. Please try again.")
      return False

  def update_accounts(self, account_list):
    self.known_accounts = [*account_list]
    return self.known_accounts
  
  def main_flow(self):
    self.is_being_used = True

    while self.is_being_used:
      print(f"\nWelcome to {self.parent_bank} - {self.address} branch ATM")
      print("Type 1 to start using this ATM branch or")
      print("Type 2 to use another location")
      choice = int(input("Enter choice [1 or 2]: "))
      
      if choice == 1:
        card_number = input("Please insert/type card number: ")
        card_is_valid = self.insert_card(card_number)

        if card_is_valid:
          self.process_transaction()
      elif choice == 2:
        self.is_being_used = False
  
  def validate_card(self, card_number):
    for i in self.known_accounts:
      if card_number == i.atm_card_num:
        return i
      else:
         continue
    return None
      
  def validate_pin(self, account):
    entered_pin = input("Enter your pin: ")
    if entered_pin == account.atm_pin:
      self.accessed_account = account
      return True
    else:
      print("PIN mismatch. Card removed. Please try again.")
      return False
  
  def choose_action(self):
    print("\nType W to withdraw")
    print("Type B to check your balance")
    print("Type D to deposit")
    print("Type C to cancel")
    print("Type T to check your transactions")
    action = input("\nPlease select an action: ").capitalize()
    
    match action:
      case "W":
        self.atm_withdraw()
      case "B":
        self.atm_check_balance()
      case "D":
        self.atm_deposit()
      case "C":
        print("Transaction cancelled.")
        self.transaction_done()
      case "T":
        self.atm_check_transactions()
      case _:
        print("Invalid input. Please try again.")
        self.transaction_done()

  def atm_withdraw(self):
    print(self.accessed_account.withdraw())
  
  def atm_check_balance(self):
    print(self.accessed_account.get_balance())
  
  def atm_deposit(self):
    print(self.accessed_account.deposit())
  
  def atm_check_transactions(self):
    transactions = self.accessed_account.get_transactions()
    for transaction in transactions:
      print(transaction)
  
  def new_transaction(self):
    print("Would you like to make another transaction? Press Y for yes and N for no.")
    go_loop = True
    while go_loop:
      action = input("Y or N: ").capitalize()
      if action == "Y":
        go_loop = False
        return True
      elif action == "N":
        go_loop = False
        return False

  def process_transaction(self):
      self.choose_action()
      another_tranction = self.new_transaction()

      if another_tranction:
        self.process_transaction()
      else:
        self.transaction_done()
    
  def transaction_done(self):
    self.accessed_account = None
    print("Thank you for banking with us!")