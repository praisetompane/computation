from impl.queue_deque_based import Queue
from threading import Thread
import time
import random


class OrderSimulation:

    def __init__(self, menu) -> None:
        self.orders = Queue()
        self.menu = menu

        self.ordering_thread = Thread(
            target=self.place_order, args=[self.menu])
        self.ordering_thread.start()

        time.sleep(1)

        self.serving_thread = Thread(
            target=self.serve_order)
        self.serving_thread.start()

    def place_order(self, menu):
        while True:
            idx = random.randint(0, len(menu) - 1)
            self.orders.enqueue(menu[idx])
            time.sleep(0.5)

    def serve_order(self):
        while True:
            print(f"serving order {self.orders.dequeue()}")
            time.sleep(2)

    def __str__(self) -> str:
        return str(self.orders.items)
