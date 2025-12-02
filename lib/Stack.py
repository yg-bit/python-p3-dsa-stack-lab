class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            return
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, target):
        try:
            # Search from the end of the stack (top) backwards
            # Return distance from top (0 if at top)
            index = len(self.items) - 1 - self.items[::-1].index(target)
            return len(self.items) - 1 - index
        except ValueError:
            # Target not found
            return -1
