from insertion_sort import InsertionSort
from mergesort import Mergesort

class HybridSort:

    @staticmethod
    def sort(arr, S):
        # Once the size of a subarray is less than or equal to a threshold (S), the algorithm switches from Mergesort to Insertion Sort
        if len(arr) <= S:
            InsertionSort.sort(arr)
        else:
            Mergesort.sort(arr)