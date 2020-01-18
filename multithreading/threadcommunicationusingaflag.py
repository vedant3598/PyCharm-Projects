from threading import *
from time import *

class Producer:

    def __init__(self):
        self.products = []
        self.ordersplaced = False

    def produce(self):
        for i in range(1, 5):
            self.products.append("Product " + str(i))
            sleep(1)
            print("Item Added")
        self.ordersplaced = True

class Consumer:

    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while self.prod.ordersplaced == False:
            print("Waiting for orders.")
            sleep(0.2)
        print("Orders Shipped: ", self.prod.products)


p = Producer()
t1 = Thread(target=p.produce)

c = Consumer(p)
t2 = Thread(target=c.consume)

t1.start()
t2.start()