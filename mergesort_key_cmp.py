from generate_input import GenerateInput
from mergesort import Mergesort

class MergesortKeyCmp:

    @staticmethod
    def average_key_cmp(size, random_tests):
        # For each size, generate 10 random datasets [1, ... , x] and take the average number of key comparisons of the 10
        average_key_cmp = 0

        for i in range(random_tests):
            initial_key_cmp = 0
            arr = GenerateInput.generate_array(size)
            final_key_cmp = Mergesort.sort(arr, initial_key_cmp)
            average_key_cmp += final_key_cmp

        average_key_cmp /= random_tests
        print(average_key_cmp)

        return average_key_cmp
    
# MergesortKeyCmp.average_key_cmp(1000, 10)