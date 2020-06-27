class RingBuffer:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.index = 0 

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.index] = item
            self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return self.items 