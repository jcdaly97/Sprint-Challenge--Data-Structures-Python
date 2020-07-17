class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.overwrite = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.overwrite] = item
            if self.overwrite + 1 == self.capacity:
                self.overwrite = 0
            else:
                self.overwrite += 1 
        else:
            self.data.append(item)

    def get(self):
        return self.data