from bank import SavingsAccount, Bank
from accounts import accounts1



def main():
    bank = Bank("Miming Bank")
    bank.load_accounts(account_list=accounts1)
    cdo_atm = bank.create_atm("Cagayan de Oro")
    manila_atm = bank.create_atm("Metro Manila")
    bank_running = True
    bank_atms = len(bank.handled_atms) 

    while bank_running:
        print(f"\n=== {bank.bank_name} ===")
        print("Choose an ATM branch")
        for i in range(bank_atms):
            print(f"Press {i} for {bank.handled_atms[i].address}")
        print(f"\n\nPress {bank_atms} to EXIT.")

        branch = int(input("Enter branch number: "))
        if branch < bank_atms:
            bank.handled_atms[branch].main_flow()
        elif branch == bank_atms:
            quit()


if __name__ == "__main__":
    main()