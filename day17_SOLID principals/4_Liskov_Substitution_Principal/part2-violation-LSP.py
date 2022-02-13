# https://www.baeldung.com/java-liskov-substitution-principle
from abc import abstractmethod

"""
Current proposed design.
                                                  BankingAppWithdrawalService  
                                                              |
                                                              | 
                                                              |
                                                             Account 
                                                          /   |      \
                                                         /    |       \
                                                        /     |        \
                                                       /      |         \
                                                      /       |          \
                                                     /        |           \              
                                                    /         |            \              
                                                   /          |             \                      
                                        SavingsAccount  LongTermAccount   CurrentAccount      
"""


# Case:1- Violates
class Account:
    total_amount = 10000

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdrawal(self, amount):
        pass


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
                amount = int(input("Please amount to  withdrawal: "))
                self.account.withdrawal(amount)
            else:
                raise Exception("Invalid selection")


class CurrentAccount(Account):

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


class SavingAccount(Account):

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


class LongTermAccount(Account):
    def deposit(self, amount):
        print(f'Deposit to saving account: {amount}')
        self.total_amount += amount
        return self.total_amount

    def withdrawal(self, amount):
        raise Exception("Withdrawal is not allowed")


server = BankingAppWithdrawalService(SavingAccount())
server1 = BankingAppWithdrawalService(CurrentAccount())
server.transaction()

# Problem
server2 = BankingAppWithdrawalService(LongTermAccount())

"""
Problem starts here because, in the base class we had two functions and it was assumed that Any class extending Account
class with have at least withdrawal and deposit functionality. But with LongTermAccount class we don't want withdrawal
functionality. Since according to LSP, If base class is replaced by any child class, there should not be any effect on 
users, but here once we replace Account class with LongTermAccount class, we get an exception while calling withdrawal 
function.
Hence, LongTermAccount class should not be member of Account class.
Technically we should have two two types of class inheriting Account class (1. with withdrawal, 2. without withdrawal 
functionality). In Account class, now we will have only deposit function.
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
                                              /       \                        /
                                             /         \                      /
                                            /           \                    /
                                    SavingsAccount    CurrentAccount      LongTermAccount
                                    
See part2-follow for LSP follow code.
"""
