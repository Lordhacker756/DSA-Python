from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.queue = deque()

    def enque(self, val):
        self.queue.appendleft(val)

    def deque(self):
        if len(self.queue) == 0:
            print("Queue empty!")
            return
        return self.queue.pop()

    def show(self):
        return self.queue

    def is_empty(self):
        return len(self.queue) == 0


def place_order(arr):
    for order in arr:
        print(f"Placing an order for {order}")
        dhaba.enque(order)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        if not dhaba.is_empty():
            dish = dhaba.deque()
            print(f"\n------- Order Ready for {dish} -------\n")
            time.sleep(2)
        else:
            print("All orders are delivered!")
            return


dhaba = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

place_orders = threading.Thread(target=place_order, args=(orders,))
# Take note, to make sure multiple elements are sent, include the ','
serve_orders = threading.Thread(target=serve_order)

place_orders.start()
serve_orders.start()

place_orders.join()
serve_orders.join()
