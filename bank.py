from atm_machine import ATM
import datetime

class SavingsAccount:
    transactions = []
    def __init__(self, account_name, account_number, atm_card_num, atm_pin, balance):
       self.account_name = account_name
       self.account_number = account_number
       self.balance = balance
       self.atm_card_num = atm_card_num
       self.atm_pin = atm_pin

    def get_balance(self):
        return f"Current balance: {self.balance}"
    
    def get_account_num(self):
        return self.account_number
    
    def get_account_name(self):
        return self.account_name
    
    def reset_pin(self):
        new_pin = input("Enter new PIN: ")
        confirmed_pin = input("Confirm new PIN: ")

        if confirmed_pin == new_pin:
          self.atm_pin = confirmed_pin
          return f"PIN reset success!"
        else:
            return f"PINs did not match. Please try again." 

    def withdraw(self):
        withdraw_amount = float(input("Enter amount to be withdrawn: "))
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            self.transactions.append({"type": "Withdrawal", "amount": withdraw_amount, "transaction_date": datetime.datetime.now()})
            return f"Successfully withdrew {withdraw_amount}. Remaining balance: {self.balance}"
        else:
            return f"Current balance is not enough. Please try a lower amount"
    
    def deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:
          self.balance += deposit_amount
          
          self.transactions.append({"type": "Deposit", "amount": deposit_amount, "transaction_date": datetime.datetime.now()})
          return f"Deposit successful! Current balance: {self.balance}"
        else:
            return f"Error: cannot deposit amounts less than 1. Please try again"
    
    def get_transactions(self):
        return self.transactions


class Bank:
    accounts = []
    handled_atms = []
    def __init__(self, bank_name):
        self.bank_name = bank_name
    
    def create_account(self):
        account_name = input("Please enter account name: ")
        account_number = input("Please enter account number: ")
        atm_card_number = input("Please enter card number: ")
        initial_balance = float(input("Enter initial balance: "))

        new_account = SavingsAccount(account_name, account_number, atm_card_number, initial_balance)
        self.accounts.append(new_account)
        if len(self.handled_atms) >= 0:
          self.update_atm_records()

    def get_accounts(self):
        return self.accounts
    
    def create_atm(self, atm_branch_or_address):
        new_atm = ATM(100_000, atm_branch_or_address, self.accounts, self.bank_name)
        self.handled_atms.append(new_atm)
        return new_atm
        # creates new atms

    def update_atm_records(self):
        for atm in self.handled_atms:
            atm.update_accounts(self.accounts)
        # updates atm account records
    
    def load_accounts(self, account_list):
        self.accounts = [*account_list]
        return self.accounts