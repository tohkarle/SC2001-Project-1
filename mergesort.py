class Mergesort:

    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            # Partition list into 2 equal size
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Mergesort left_half and right_half
            Mergesort.sort(left_half)
            Mergesort.sort(right_half)
            Mergesort.merge(arr, left_half, right_half)

    @staticmethod
    def merge(arr, left_half, right_half):
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