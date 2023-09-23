"""
Run your program of the hybrid algorithm on the datasets generated in Step (b).
Record the number of key comparisons performed in each case.

i. With the value of S fixed, plot the number of key comparisons over different sizes of the input list n. 
Compare your empirical results with your theoretical analysis of the time complexity.

ii. With the input size n fixed, plot the number of key comparisons over different values of S. 
Compare your empirical results with your theoretical analysis of the time complexity.

iii. Using different sizes of input datasets, study how to determine an optimal value of S for the best performance of this hybrid algorithm.
"""

from generate_input import GenerateInput
from hybrid_sort import HybridSort
from mergesort_key_cmp import MergesortKeyCmp
from insetion_sort_key_cmp import InsertionSortKeyCmp
import numpy as np

class HybridSortKeyCmp:

    @staticmethod
    def average_key_cmps_with_s_fixed(min_input_size, max_input_size, s_fixed, random_tests):
        # S fixed at 99 (TBC)
        # Input size range from 1000 to 10000000
        # input_sizes = []
        average_key_cmps = []
        num_points = 100

        # for i in range(min_input_size, max_input_size + 1, int((max_input_size - min_input_size) / num_points)):
            # input_sizes.append(i)

        # Generate input sizes on a logarithmic scale
        input_sizes = np.logspace(np.log10(min_input_size), np.log10(max_input_size), num=num_points, dtype=int)
        input_sizes = list(dict.fromkeys(input_sizes))

        for input_size in input_sizes:
            average_key_cmp = HybridSortKeyCmp.average_key_cmp(input_size, s_fixed, random_tests)
            average_key_cmps.append(average_key_cmp)

        # print(input_sizes)
        # print(average_key_cmps)

        return input_sizes, average_key_cmps
    

    @staticmethod
    def average_key_cmps_with_n_fixed(min_s, max_s, input_size_fixed, random_tests):
        # Input size fixed at 1000 (TBC)
        # S value range from 1 to 1000
        average_key_cmps = []
        s_values = []
        num_points = 100

        for i in range(min_s, max_s + 1):
            s_values.append(i)

        for s_value in s_values:
            average_key_cmp = HybridSortKeyCmp.average_key_cmp(input_size_fixed, s_value, random_tests)
            average_key_cmps.append(average_key_cmp)

        # print(s_values)
        # print(average_key_cmps)

        return s_values, average_key_cmps


    @staticmethod
    def average_key_cmps_for_optimal_s(min_input_size, max_input_size, random_tests):
        # S value is essentially the threshold array size in which Insertion sort performs better than Mergesort
        # For determining optimal S, we are going to plot Average Key Cmp VS Array Size (S) for both Insertion Sort and Mergesort
        mergesort_average_key_cmps = []
        insertion_sort_average_key_cmps = []
        array_sizes = []

        for i in range(min_input_size, max_input_size + 1):
            array_sizes.append(i)

        for array_size in array_sizes:
            mergesort_average_key_cmp = MergesortKeyCmp.average_key_cmp(array_size, random_tests)
            insertion_sort_average_key_cmp = InsertionSortKeyCmp.average_key_cmp(array_size, random_tests)
            mergesort_average_key_cmps.append(mergesort_average_key_cmp)
            insertion_sort_average_key_cmps.append(insertion_sort_average_key_cmp)

        return array_sizes, mergesort_average_key_cmps, insertion_sort_average_key_cmps


    @staticmethod
    def average_key_cmp(size, S, random_tests):
        # For each size, generate 10 random datasets [1, ... , x] and take the average number of key comparisons of the 10
        average_key_cmp = 0

        for i in range(random_tests):
            initial_key_cmp = 0
            arr = GenerateInput.generate_array(size)
            final_key_cmp = HybridSort.sort(arr, S, initial_key_cmp)
            average_key_cmp += final_key_cmp

        average_key_cmp /= random_tests
        # print(average_key_cmp)
        return average_key_cmp

    
# HybridSortKeyCmp.average_key_cmps_with_n_fixed(2, 20, 1000, 1)
# HybridSortKeyCmp.average_optimal_s_values(2, 20, 1000, 10000000, 1)
# HybridSortKeyCmp.average_key_cmps_with_s_fixed(1000, 10000000, 99, 1)
# HybridSortKeyCmp.average_key_cmps_for_optimal_s(2, 100, 10)