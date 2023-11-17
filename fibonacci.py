class FibonacciGenerator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_index = 0
        self.prev_number = 0
        self.curr_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < 2:
            result = self.current_index
        else:
            result = self.prev_number + self.curr_number

        if self.current_index >= self.max_count:
            raise StopIteration
        if self.current_index >= 2:
            self.prev_number, self.curr_number = self.curr_number, result
        self.current_index += 1
        return result

def display_fibonacci_sequence(sequence_length):
    fib_seq = FibonacciGenerator(sequence_length)
    for val in fib_seq:
        print(val)

if __name__ == "__main__":
    sequence_length = int(input('How many Fibonacci numbers to display: '))
    print('Fibonacci Sequence:')
    display_fibonacci_sequence(sequence_length)