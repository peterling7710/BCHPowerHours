# Create a definition of a bank account, and its functionality
class Account():
    def __init__(self, num, type):
        self.funds = 0
        self.num = num
        self.type = type
    
    def deposit(self, amount):
        self.funds += amount

    def check_funds(self, amount):
       return 1 if self.funds < amount else 0
            
    def withdraw(self, amount):
        flag = self.check_funds(amount)
        if flag:
            print('Overdraft warning!')
        else:
            self.funds -= amount
    
    def transfer(self, account, amount):
        flag = self.check_funds(amount)
        if flag:
            print('Overdraft warning!')
        else:
            self.funds -= amount
            account.funds += amount
    
    def summary(self):
        return (f'{self.type} account. Number: {self.num}. Total funds: ${self.funds}')

def check_account(accounts):
    if len(accounts) == 0:
        print('No accounts created')
        return
    elif len(accounts) > 1:
        num = int(input('Please enter the index or the account number of the account you wish to use\n'))
        for i, account in enumerate(accounts):
            if num == account.num or num == i:
                target = account
    else:
        target = accounts[0]
    return target

#Create a loop that only breaks when the exit button is pressed
if __name__ == '__main__':
    accounts = []
    message = ('Welcome to my bank account tracking applet\n'
        'Press the following buttons to perform the respective command\n'
        '0. Exit\n'
        '1. Add an account\n'
        '2. Deposit funds\n'
        '3. Withdraw funds\n'
        '4. Transfer funds between accounts\n'
        '5. A summary of a single account\n'
        '6. A summary of all accounts \n'
        '7. Your total funds across all accounts\n'
        '8. Delete an account\n')

    while True:
        # Display the options to the user
        # Ask for input
        option = input(message)
        try:
            # Check if the app should exit
            option = int(option)
            if option == 0:
                print('exiting')
                break

            # Check which option was selected
            # Perform the correct task
            elif option == 1:
                # Add new account
                account = input('Enter the account number and type, separated by a comma\n')
                account = account.split(',')
                new_account = Account(int(account[0]), account[1].strip())
                accounts.append(new_account)

            elif option == 2:
                # Deposit
                account = check_account(accounts)
                amount = input('Enter the deposit amount\n')
                try:
                    account.deposit(float(amount))
                except:
                    pass

            elif option == 3:
                # Withdraw
                account = check_account(accounts)
                amount = input('Enter the withdrawl amount\n')
                try:
                    account.withdraw(float(amount))
                except:
                    pass

            elif option == 4:
                # Transfer
                if len(accounts) <2:
                    print('Not enough accounts to transfer funds')
                else:
                    withdraw = int(input('Enter the account number/index you wish to withdraw from\n'))
                    deposit = int(input('Enter the account number/index you wish to deposit to\n'))
                    for i, account in enumerate(accounts):
                        if withdraw == account.num or withdraw == i:
                            withdraw_account = account
                        if deposit == account.num or deposit == i:
                            deposit_account = account
                    amount = float(input('Enter the transfer amount\n'))
                    withdraw_account.transfer(deposit_account, amount)

            elif option == 5:
                # Single summary
                account = check_account(accounts)
                try:
                    print(account.summary())
                except:
                    pass

            elif option == 6:
                # Summary all
                for i, account in enumerate(accounts):
                    s = f'{i+1}. ' + account.summary()
                    print(s)

            elif option == 7:
                # Total funds
                s = 0
                for account in accounts:
                    s += account.funds
                print(f'total funds: ${s}')
            
            elif option == 8:
                # Delete Account
                account = check_account(accounts)
                try:
                    i = accounts.index(account)
                    del accounts[i]
                except:
                    pass

            else:
                print('Invalid entry, try again')

        except ValueError as e:
            print('Invalid entry, try again')
