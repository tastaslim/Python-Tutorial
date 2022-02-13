# https://www.baeldung.com/java-liskov-substitution-principle
from abc import abstractmethod

"""
Follow LSP.
                                                BankingAppWithdrawalService  
                                                             |
                                                             | 
                                                             |
                                                           Account 
                                                          /       \
                                                         /         \
                                                        /           \
                                                       /             \
                                                      /               \
                                                     /                 \              
                                                    /                   \              
                                                   /                     \              
                                        WithoutWithdrawalAccount     WithWithdrawalAccount 
                                              /       \                    /          \
                                             /         \                  /            \
                                            /           \                /              \
                                    SavingsAccount    CurrentAccount  LongTermAccount   RetirementAccount
"""


# Follow - LSP
# noinspection DuplicatedCode

class BankingAppWithdrawalService:
    def __init__(self, account):
        self.account = account

    def transaction(self):
        pin = int(input('Please enter your pin: '))
        if pin == 1234:
            print('Transaction started...')
            choice = input("Enter your choice: ")
            if choice == "deposit":
                amount = int(input("Please amount to  deposit: "))
                self.account.deposit(amount)
            elif choice == "withdrawal":
                if isinstance(self.account, WithWithdrawalAccount):
                    amount = int(input("Please amount to  withdrawal: "))
                    self.account.withdrawal(amount)
                else:
                    print("Withdrawal disabled")
            else:
                print("Invalid choice")


class Account:
    total_amount = 10000

    @abstractmethod
    def deposit(self, amount):
        pass


class WithoutWithdrawalAccount(Account):
    def deposit(self, amount):
        pass


class WithWithdrawalAccount(Account):
    def deposit(self, amount):
        pass

    def withdrawal(self, amount):
        pass


class CurrentAccount(WithWithdrawalAccount):

    def deposit(self, amount):
        print(f'Deposit to current account: {amount}')
        self.total_amount += amount
        return self.total_amount

    def withdrawal(self, amount):
        print(f'Withdrawal to current account: {amount}')
        if self.total_amount <= 5000 or self.total_amount < amount:
            return f"Can't withdraw amount: {amount}. Insufficient balance"
        self.total_amount -= amount
        return self.total_amount


class SavingAccount(WithWithdrawalAccount):

    def deposit(self, amount):
        print(f'Deposit to saving account: {amount}')
        self.total_amount += amount
        return self.total_amount

    def withdrawal(self, amount):
        print(f'Deposit to saving account: {amount}')
        if self.total_amount <= 0 or self.total_amount < amount:
            return f"Can't withdraw amount: {amount}. Insufficient balance"
        self.total_amount -= amount
        return self.total_amount


class LongTermAccount(WithoutWithdrawalAccount):
    def deposit(self, amount):
        print(f'Deposit to saving account: {amount}')
        self.total_amount += amount
        return self.total_amount


class RetirementAccount(WithoutWithdrawalAccount):
    def deposit(self, amount):
        print(f'Deposit to saving account: {amount}')
        self.total_amount += amount
        return self.total_amount


server = BankingAppWithdrawalService(WithoutWithdrawalAccount())
server.transaction()
