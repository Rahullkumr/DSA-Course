def binary_search(arr, no_to_search):
    '''Binarry search works only with sorted arrays
        binary_search: search the array and return the element if present
        arr: the given sorted array
        no_to_search: the number to be searched
    '''
    left = 0
    right = len(arr) - 1
    while arr[left] <= arr[right]:
        mid = (left + right) // 2

        if no_to_search == arr[mid]:
            # If found at middle index then return mid + 1
            return mid + 1

        if no_to_search > arr[mid]:
            # Search in right half of current subarray
            left = mid + 1
        else:
            # Search in left half of current subarray
            right = mid - 1
    return -1




array = [1,2,3,4,5,6,7,8]
SEARCHME = 1
at = binary_search(array, SEARCHME)
print(f'present at : {at}th position')
