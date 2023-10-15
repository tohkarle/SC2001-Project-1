"""
Generate arrays of increasing sizes, in a range from 1,000 to 10 million. 
For each of the sizes, generate a random dataset of integers in the range of [1, …, x], where x is the largest number you allow for your datasets.
"""

import random

class GenerateInput:
    MIN_VALUE = 1

    # Decided to use this as the value of x because if x is too small, there will be a lot of repeated elements in array of size 10_000_000
    MAX_VALUE = 100_000_000

    @staticmethod
    def generate_array(size):
        return [random.randint(GenerateInput.MIN_VALUE, GenerateInput.MAX_VALUE) for _ in range(size)]