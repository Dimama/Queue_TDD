
class Triplet(object):
    def __init__(self, value, maximum, minumum):
        self.value = value
        self.max_val = maximum
        self.min_val = minumum

class Stack(object):

    def __init__(self, items=[]):
        self.items = []
        for item in reversed(items):
            self.push(item)

    def push(self, item):
        if self.is_empty():
            min_value = item
            max_value = item
        else:
            min_value = min(self.top().min_val, item)
            max_value = max(self.top().max_val, item)

        self.items.insert(0, Triplet(item, max_value, min_value))

    def pop(self):
        return self.items.pop(0).value

    def top(self):
        return self.items[0]

    def is_empty(self):
        return not bool(len(self.items))

    def min(self):
        return self.top().min_val

    def max(self):
        return self.top().max_val
