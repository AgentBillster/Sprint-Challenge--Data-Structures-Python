class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.increment = 0

    def reset_increment(self):
        self.increment = 0

    def append(self, item):
        # is storage at capacity?
        # if so just regular append item.
        # otherwise i need to start replacing items at index
        # i am going to start with [0] then [1] then [2] until we get to capacty
        # when we are at capacity then set the increment back to 0 AND THEN I THINK THIS WILL WOOOOORRR
        # GETTTING AN ERROR WHATS WRONG COME BACK LATER
        if len(self.storage) is not self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.increment] = item
            self.increment += 1
            if self.increment is self.capacity:
                self.reset_increment()

    def get(self):
        return self.storage
