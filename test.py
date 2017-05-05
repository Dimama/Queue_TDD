import unittest
from queue import Queue


""" 
    Ожидаемые результаты тестов:
    max_lst: результаты метода maximum()
    min_lst: результаты метода minimum()
    en_lst: состояния очередей в рез-те вызова метода enqueue() с соотв. элементом из en_items
    de_lst: состояния очередей в рез-те вызова метода dequeue() 
    de_items: элементы, удаленные из очередей в результате вызова метода dequeue()
"""
max_lst = [3, 4, None, 5, 96, 0, 11]
min_lst = [1, 1, None, 5, 9, 0, 3]
en_items = [0, 20, 7, 777, 9, 8, 500]
en_lst = [
    [0, 1, 2, 3],
    [20, 1, 2, 3, 4],
    [7],
    [777, 5, 5, 5, 5, 5, 5],
    [9, 9, 19, 12, 23, 80, 96, 10, 96],
    [8, 0, 0],
    [500, 3, 11, 10, 9, 8, 7, 6, 5, 3]
]
de_items = [3, 4, None, 5, 96, 0, 3]
de_lst = [
    [1, 2],
    [1, 2, 3],
    [],
    [5, 5, 5, 5, 5],
    [9, 19, 12, 23, 80, 96, 10],
    [0],
    [3, 11, 10, 9, 8, 7, 6, 5, ]
]


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = [[]]*7
        self.queue[0] = Queue([1, 2, 3])
        self.queue[1] = Queue([1, 2, 3, 4])
        self.queue[2] = Queue()
        self.queue[3] = Queue([5, 5, 5, 5, 5, 5])
        self.queue[4] = Queue([9, 19, 12, 23, 80, 96, 10, 96])
        self.queue[5] = Queue([0, 0])
        self.queue[6] = Queue([3, 11, 10, 9, 8, 7, 6, 5, 3])

    def testMaximum(self):
        for i in range(len(max_lst)):
            with self.subTest("exp.max: {0}, queue: {1}".format(max_lst[i], self.queue[i].get_items().__str__())):
                self.assertEqual(self.queue[i].maximum(), max_lst[i])

    def testMinimum(self):
        for i in range(len(min_lst)):
            with self.subTest("exp.min: {0}, queue: {1}".format(min_lst[i], self.queue[i].get_items().__str__())):
                self.assertEqual(self.queue[i].minimum(), min_lst[i])

    def testEnqueue(self):
        for i in range(len(en_items)):
            self.queue[i].enqueue(en_items[i])
            with self.subTest("exp.queue: {0}, queue: {1}".format(en_lst[i], self.queue[i].get_items().__str__())):
                self.assertEqual(self.queue[i].get_items(), en_lst[i])

    def testDequeue(self):
        for i in range(len(de_items)):
            item = self.queue[i].dequeue()
            with self.subTest("exp.queue: {0}, queue: {1}".format(de_lst[i], self.queue[i].get_items().__str__())):
                self.assertEqual(self.queue[i].get_items(), de_lst[i])
                self.assertEqual(item, de_items[i])

if __name__ == "main":
    t1 = TestQueue()
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(t1))
    runner = unittest.TextTestRunner()
    runner.run(suite)