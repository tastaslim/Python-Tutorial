from abc import abstractmethod


class Transport:
    @abstractmethod
    def factory_method(self):
        pass

    @abstractmethod
    def deliver(self):
        return self.factory_method()


class Car(Transport):
    def factory_method(self):
        return Car()

    def deliver(self):
        return 'Deliver by car'


class Train(Transport):
    def factory_method(self):
        return Train()

    def deliver(self):
        return 'Deliver by train'


class Ship(Transport):
    def factory_method(self):
        return Ship()

    def deliver(self):
        return 'Deliver by ship'


class ClientCode:
    def __init__(self, transportation: Transport):
        self.transport = transportation

    def delivery(self):
        print(self.transport.deliver())


if __name__ == "__main__":
    client = ClientCode(Car())
    client.delivery()

    # client = ClientCode(Train())
    # client.delivery()
    #
    # client = ClientCode(Ship())
    # client.delivery()
