class LegacyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current


my_iterator = LegacyIterator(10)
for item in my_iterator:
    print(item)
