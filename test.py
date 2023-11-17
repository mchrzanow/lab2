import time
import random
from multiprocessing import cpu_count
import matplotlib.pyplot as plt
from sort import SortowanieRownolegle

class SorterPerformanceTester:
    def __init__(self):
        self.timing_results = {}

    def run_performance_test(self, sizes_to_test, num_processes):
        for proc_count in num_processes:
            measured_times = [self.time_sort(size, proc_count) for size in sizes_to_test]
            self.timing_results[proc_count] = measured_times

    def time_sort(self, data_size, num_proc):
        dataset = [random.randint(0, data_size) for _ in range(data_size)]
        sorter_instance = SortowanieRownolegle(dataset)
        start = time.time()
        sorter_instance.sortuj(liczba_procesow=num_proc)
        end = time.time()
        return end - start

    def display_results(self, sizes_to_test):
        figure, axis = plt.subplots()
        for proc_count, timings in self.timing_results.items():
            axis.plot(sizes_to_test, timings, marker='o', label=f'{proc_count} Processes')

        axis.set_xlabel('Data Size')
        axis.set_ylabel('Time (seconds)')
        axis.set_title('Sorting Performance with Different Processes')
        axis.legend(loc='upper left')
        plt.show()

if __name__ == "__main__":
    performance_tester = SorterPerformanceTester()
    sizes_to_evaluate = [10, 500, 1000, 5000]
    possible_process_counts = [1, 2, 4, cpu_count()]

    performance_tester.run_performance_test(sizes_to_evaluate, possible_process_counts)
    performance_tester.display_results(sizes_to_evaluate)
