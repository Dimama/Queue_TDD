from queue import Queue
from random import randint
import msvcrt
import sys

def change(queue):
    item = randint(0, 100)
    queue.dequeue()
    queue.enqueue(item)
    print("\n------------------------")
    print("Random number: {0}".format(item))
    print("Queue: {0}".format(queue.get_items()))
    print("Max: {0}, Min: {1}".format(queue.maximum(), queue.minimum()))

def main():

    SIZE = 10
    q = Queue()
    for i in range(SIZE):
        q.enqueue(randint(0, 100))
    print("Start queue: {0}".format(q.get_items()))
    print("Press any key to update queue, press 'q' to exit.")


    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch()
            if ch == 'q':
                sys.exit()
            else:
                change(q)

if __name__ == "__main__":
    main()




