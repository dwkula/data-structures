"""
For all exercises use Queue class implemented in main tutorial.

    Design a food ordering system where your python program will run two threads,
        Place Order: This thread will be placing an order and inserting that into a queue. 
        This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)

        Serve Order: This thread will server the order. 
        All you need to do is pop the order out of the queue and print it. 
        This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

    Pass following list as an argument to place order thread,

    orders = ['pizza','samosa','pasta','biryani','burger']

    This problem is a producer,consumer problem where place_order thread is producing orders 
    whereas server_order thread is consuming the food orders. 

"""
from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


orders_que = Queue()


def place_order(orders):

    for element in orders:

        orders_que.enqueue(element)
        print(f'Order {element} added to queue')
        time.sleep(0.5)


def server_order():
    time.sleep(1)
    while True:
        print(f'Now serving: { orders_que.dequeue() } ')
        time.sleep(2)


order = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

t1 = threading.Thread(target=place_order, args=(order,))
t2 = threading.Thread(target=server_order)
