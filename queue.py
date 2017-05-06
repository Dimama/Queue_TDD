from stack import Stack


class Queue(object):

    def __init__(self, items=[]):
        self.in_stack = Stack(items)
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not (self.in_stack.is_empty()):
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def maximum(self):
        if self.is_empty():
            return None
        if self.in_stack.is_empty() or self.out_stack.is_empty():
            if self.in_stack.is_empty():
                return self.out_stack.top().max_val
            return self.in_stack.top().max_val
        else:
            return max(self.out_stack.top().max_val, self.in_stack.top().max_val)

    def minimum(self): 
        if self.is_empty():
            return None
        if self.in_stack.is_empty() or self.out_stack.is_empty():
            if self.in_stack.is_empty():
                return self.out_stack.top().min_val
            return self.in_stack.top().min_val
        else:
            return min(self.out_stack.top().min_val, self.in_stack.top().min_val)

    def size(self):
        return len(self.out_stack.items) + len(self.in_stack.items)

    def is_empty(self):
        return self.out_stack.is_empty() and self.in_stack.is_empty()

    def get_items(self):
        res = []
        for i in self.in_stack.items:
            res.append(i.value)
        for i in reversed(self.out_stack.items):
            res.append(i.value)
        return res
