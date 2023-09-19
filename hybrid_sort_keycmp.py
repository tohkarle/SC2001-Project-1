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

    S_FIXED = 99
    MIN_INPUT_SIZE = 1000
    MAX_INPUT_SIZE = 10_000_000

    INPUT_SIZE_FIXED = 1000
    MIN_S = 1
    MAX_S = 1000

    DATASETS = 10

    def average_key_cmps_with_s_fixed():
        # S fixed at 99 (TBC)
        # Input size range from 1000 to 10000000
        averageKeyCmps = []
        num_points = 100

        # Generate input sizes on a logarithmic scale
        sizes = np.logspace(np.log10(HybridSortKeyCmp.MIN_INPUT_SIZE), np.log10(HybridSortKeyCmp.MAX_INPUT_SIZE), num=num_points, dtype=int)

        for size in sizes:
            averageKeyCmp = HybridSortKeyCmp.average_key_cmp(size)
            averageKeyCmps.append(averageKeyCmp)

        print(sizes)
        print(averageKeyCmps)

        return averageKeyCmps
    

    def average_key_cmps_with_n_fixed():
        # Input size fixed at 1000 (TBC)
        # S value range from 1 to 1000
        averageKeyCmps = []
        s_values = []
        num_points = 100

        # Genearate different S values on a logarithmic scale
        s_values = np.logspace(np.log10(HybridSortKeyCmp.MIN_S), np.log10(HybridSortKeyCmp.MAX_S), num=num_points, dtype=int)

        for s_value in s_values:
            averageKeyCmp = HybridSortKeyCmp.average_key_cmp(S = s_value)
            averageKeyCmps.append(averageKeyCmp)

        print(s_values)
        print(averageKeyCmps)

        return averageKeyCmps


    def average_key_cmp(size = INPUT_SIZE_FIXED, S = S_FIXED):
        # For each size, generate 10 random datasets [1, ... , x] and take the average number of key comparisons of the 10
        averageKeyCmp = 0

        for i in range(HybridSortKeyCmp.DATASETS):
            initialKeyCmp = 0
            arr = GenerateInput.generate_array(size)
            finalKeyCmp = HybridSort.sort(arr, S, initialKeyCmp)
            print(finalKeyCmp)
            averageKeyCmp += finalKeyCmp

        averageKeyCmp /= HybridSortKeyCmp.DATASETS
        print(averageKeyCmp)
        return averageKeyCmp