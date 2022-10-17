class Fibonacci():
    def __init__(self, initial_num):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b

    def __iter__(self):
        return self

fibonacci_num = Fibonacci(1)
print(next(fibonacci_num))
print(next(fibonacci_num))
print(next(fibonacci_num))
print(next(fibonacci_num))
