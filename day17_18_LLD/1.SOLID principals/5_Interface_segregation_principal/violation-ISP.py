"""
Many client-specific interfaces are better than one general-purpose interface.
Which means that we should not write single interface, put everything inside it and let all classes
implement this, because ultimately class which don't need any specific feature they are forced to implement
those functions.
Because we don't want our client to dependent on those functions/properties which it does not need.
Ultimately they will be either throwing an error saying that method not implemented or something which is wastage
of code and memory, not productive and your clients might get surprising results.
"""
# ISP- violation:
from abc import abstractmethod


class Printer:
    @abstractmethod
    def print_data(self):
        pass

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def fax(self):
        pass


class PremiumPrinter(Printer):
    def print_data(self):
        print("Premium printer")

    def scan(self):
        print("Premium scanner")

    def fax(self):
        print("Premium faxing")

    @staticmethod
    def premium():
        print("Premium features. Exclusive")


class NormalPrinter(Printer):
    def print_data(self):
        print("Normal printer")

    def scan(self):
        print("Normal scanner")

    def fax(self):
        print("Normal faxing")


class OldPrinter(Printer):
    def print_data(self):
        print("Premium printer")

    def scan(self):
        raise Exception("Scanning feature not available")  # raise error feature not available

    def fax(self):
        raise Exception("faxing feature not available")  # raise error feature not available


"""
Here comes the problem because now users who are using old printer, they will also see scan and fax feature and when 
they try to use those, they will get warning or some weired results, which we don't want.

Ideally, we should define the features as class and let other classes inherit those which are supposed to.
see part-2
"""
