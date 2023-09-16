"""
Generate arrays of increasing sizes, in a range from 1,000 to 10 million. 
For each of the sizes, generate a random dataset of integers in the range of [1, …, x], where x is the largest number you allow for your datasets.
"""

import random

class GenerateInput:
    MIN_VALUE = 1

    @staticmethod
    def generate_array(size, max_value):
        return [random.randint(GenerateInput.MIN_VALUE, max_value) for _ in range(size)]