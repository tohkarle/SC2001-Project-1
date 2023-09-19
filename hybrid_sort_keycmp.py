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
import numpy as np

class HybridSortKeyCmp:

    @staticmethod
    def average_key_cmps_with_s_fixed(min_input_size, max_input_size, s_fixed, random_tests):
        # S fixed at 99 (TBC)
        # Input size range from 1000 to 10000000
        average_key_cmps = []
        num_points = 100

        # Generate input sizes on a logarithmic scale
        input_sizes = np.logspace(np.log10(min_input_size), np.log10(max_input_size), num=num_points, dtype=int)

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

        # Genearate different S values on a logarithmic scale
        s_values = np.logspace(np.log10(min_s), np.log10(max_s), num=num_points, dtype=int)

        for s_value in s_values:
            average_key_cmp = HybridSortKeyCmp.average_key_cmp(input_size_fixed, s_value, random_tests)
            average_key_cmps.append(average_key_cmp)

        # print(s_values)
        # print(average_key_cmps)

        return s_values, average_key_cmps


    @staticmethod
    def average_key_cmp(size, S, random_tests):
        # For each size, generate 10 random datasets [1, ... , x] and take the average number of key comparisons of the 10
        average_key_cmp = 0

        for i in range(random_tests):
            initial_key_cmp = 0
            arr = GenerateInput.generate_array(size)
            final_key_cmp = HybridSort.sort(arr, S, initial_key_cmp)
            print(final_key_cmp)
            average_key_cmp += final_key_cmp

        average_key_cmp /= random_tests
        return average_key_cmp
    
# HybridSortKeyCmp.average_key_cmps_with_n_fixed(1, 1000, 1000, 10)