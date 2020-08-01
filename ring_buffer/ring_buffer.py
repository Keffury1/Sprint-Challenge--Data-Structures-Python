class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.length = 0
        self.array = []

    def append(self, item):
        if self.length is self.capacity:
            self.array[self.index] = item
            self.index += 1
        else:
            self.array.append(item)
            self.length += 1
        
        if self.index is self.capacity:
            self.index = 0

    def get(self):
        return self.array