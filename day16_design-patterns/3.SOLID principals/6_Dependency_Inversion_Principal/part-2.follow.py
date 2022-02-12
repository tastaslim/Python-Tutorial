from abc import abstractmethod


class PaymentProcessor:
    @abstractmethod
    def list_details(self):
        pass

    @abstractmethod
    def do_payment(self, details):
        pass


class Stripe(PaymentProcessor):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def list_details(self):
        return f"Details are {self.name} and {self.amount}"

    def do_payment(self, details):
        print(f"Stripe Payment of amount {self.amount} is completed for {details}")


class PayPal(PaymentProcessor):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def list_details(self):
        return f"Paypal: Details are {self.name} and {self.amount}"

    def do_payment(self, details):
        print(f"PayPal Payment of amount {self.amount} is completed for {details}")


class Store:
    def __init__(self, payment_method: PaymentProcessor):
        self.payment = payment_method

    def payment_process(self, name, amount):
        print(f"Payment of amount {amount} started for {name}")
        details = self.payment.list_details()
        self.payment.do_payment(details)
        print("Payment is done")


s = Store(PayPal("Book", 1500))  # Now while initialising Store class, pass PaymentProcess method
s.payment_process("Book", 1500)  # payment for PayPal
s1 = Store(Stripe("Wine", 2000))
s1.payment_process("Wine", 2000)

"""
Now in future if any changes in Stripe is needed, or we want to change payment method, it
won't affect our Store service and Store Service is now talking to PaymentProcessor class.
"""
