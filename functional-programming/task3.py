class FibIterator:
    def __init__(self):
        self.counter = 100
        self.currentNum = 0
        self.nextNum = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        elif self.counter == 100:
            self.counter -= 1
            return 0

        self.counter -= 1
        self.currentNum, self.nextNum = self.nextNum, self.currentNum + self.nextNum
        return self.currentNum


def fib_generator():
    counter = 100
    currentNum = 0
    nextNum = 1
    while counter > 0:
        if counter == 100:
            counter -= 1
            yield 0
        counter -= 1
        currentNum, nextNum = nextNum, currentNum + nextNum
        yield currentNum


def strange_decorator(func):
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) > 10:
            raise ValueError
        if any(map(lambda x: isinstance(x, bool), kwargs.values())):
            raise TypeError
        func_res = func(*args, **kwargs)
        return func_res + 13 if isinstance(func_res, int) else func_res

    return wrapper
