from insertion_sort import InsertionSort
from mergesort import Mergesort

class HybridSort:

    @staticmethod
    def sort(arr, S, keyCmp):
    
        # Once the size of a subarray is less than or equal to a threshold (S), the algorithm switches from Mergesort to Insertion Sort
        if len(arr) <= S:
            return InsertionSort.sort(arr, keyCmp)
        else:
            # Partition list into 2 equal size
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Mergesort left_half and right_half
            return HybridSort.sort(left_half, S, keyCmp) + HybridSort.sort(right_half, S, keyCmp) + Mergesort.merge(arr, left_half, right_half, keyCmp)
        