def hybrid_sort(arr, S):
    # Once the size of a subarray is less than or equal to a threshold (S), the algorithm switches from Mergesort to Insertion Sort
    if len(arr) <= S:
        insertion_sort(arr)
    else:
        merge_sort(arr)

def merge_sort(arr):
    if len(arr) > 1:

        # Partition list into 2 equal size
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Mergesort left_half and right_half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Compare the first element of the 2 halves
        while i < len(left_half) and j < len(right_half):

            # If left_half[i] is smaller, left_half[i] joins the end of the merged list
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            
            # Else if right_half[j] is smaller, right_half[j] joins the end of the merged list
            else:
                arr[k] = right_half[j]
                j += 1
            
            k += 1

        # For the left over left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # For the left over right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key