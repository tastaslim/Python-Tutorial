from abc import abstractmethod


class Printer:
    @abstractmethod
    def printing(self):
        pass


class Scanner:
    @abstractmethod
    def scan(self):
        pass


class Fax:
    @abstractmethod
    def fax(self):
        pass


class PremiumPrinter(Printer, Scanner, Fax):
    def printing(self):
        print("Premium printer")

    def scan(self):
        print("Premium scanner")

    def fax(self):
        print("Premium faxing")


class OldPrinter(Printer):
    def printing(self):
        print("Old printer")


class NormalPrinter(Printer, Scanner):
    def printing(self):
        print("Premium printer")

    def scan(self):
        print("Premium scanner")
