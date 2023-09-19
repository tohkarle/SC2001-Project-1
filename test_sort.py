from insertion_sort import InsertionSort
from mergesort import Mergesort
from hybrid_sort import HybridSort

class TestSort:
    TEST_CASES = [
        [5, 2, 9, 3, 6],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [14, 40, 31, 28, 3, 15, 17, 51],
        [23, 23, 23, 23, 23, 23, 23, 23],
        [],
        [7],
    ]

    @staticmethod
    def test(sort_function):
        for test_case in TestSort.TEST_CASES:
            # Create a copy of the test case to keep the original data intact
            arr = test_case.copy()

            # Sort the array using your merge_sort function
            keyCmp = 0
            if sort_function is HybridSort.sort:
                totalKeyCmp = sort_function(arr, 3, keyCmp)
            else:    
                totalKeyCmp = sort_function(arr, keyCmp)

            # Check if the sorted array is in ascending order
            assert arr == sorted(test_case), f"Test failed for input: {test_case}"

            # Print the sorted array
            print(f"Input: {test_case}, Sorted: {arr}")
            print(f"Number of key comparisons: {totalKeyCmp}")


# TestSort.test(InsertionSort.sort)
# TestSort.test(Mergesort.sort)
TestSort.test(HybridSort.sort)
