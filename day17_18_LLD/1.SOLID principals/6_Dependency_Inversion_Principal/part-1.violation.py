class Stripe:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def list_details(self):
        return f"Details are {self.name} and {self.amount}"

    def do_payment(self, details):
        print(f"Payment of amount {self.amount} is completed for {details}")


class Store:
    def __init__(self):
        pass

    @staticmethod
    def payment_process(name, amount):
        print(f"Payment of amount {amount} started for {name}")
        stripe = Stripe(name, amount)  # wrong approach
        details = stripe.list_details()
        stripe.do_payment(details)
        print("Payment is done")


s = Store()
s.payment_process("Book", 1500)

"""
Now in future if any changes in Stripe is needed, or we want to change payment method, it
will directly affect our Store service and we need to make changes everywhere in Store Service
too.
"""
