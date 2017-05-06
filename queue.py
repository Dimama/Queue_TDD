from stack import Stack

class Queue(object):

    def __init__(self, items=[]):
        self.in_stack = Stack(items)
        self.out_stack = Stack()

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def maximum(self):
        pass

    def minimum(self): 
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

    def get_items(self):
        res = []
        for i in self.in_stack.items:
            res.append(i.value)
        for i in reversed(self.out_stack.items):
            res.append(i.value)
        return res
