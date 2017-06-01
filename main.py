from queue import Queue
from random import randint, uniform
import msvcrt
import sys

from threading import Timer, Thread, Event
import time
import _thread


def change(queue):
    item = randint(0, 100)
    queue.dequeue()
    queue.enqueue(item)
    print("\n------------------------")
    print("Random number: {0}".format(item))
    print("Queue: {0}".format(queue.get_items()))
    print("Max: {0}, Min: {1}".format(queue.maximum(), queue.minimum()))


def print_queue(queue):
    while True:
        print("\n------------------------")
        print("Queue: {0} Max: {1}, Min: {2}".format(queue.get_items(), queue.maximum(), queue.minimum()))
        time.sleep(5)


def generate(queue, values):
    while True:
        item = randint(0, 100)
        values.append(item)
        queue.dequeue()
        queue.enqueue(item)
        print("\n------------------------")
        print("Random number: {0}".format(item))
        print("Last 10 values: ", values[-10:])
        time.sleep(uniform(1.0, 5.0))


def main():
    size = 10
    q = Queue()
    values = []
    for i in range(size):
        q.enqueue(randint(0, 100))

    Thread(target=print_queue, args=(q, )).start()
    Thread(target=generate, args=(q, values)).start()


if __name__ == "__main__":
    main()



