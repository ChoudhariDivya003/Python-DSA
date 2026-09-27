def first_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            first = mid
            high = mid - 1

        elif key > arr[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return first


# Test cases

print(first_occurrence([10, 20, 20, 20, 30, 40], 20))  # 1
print(first_occurrence([10, 20, 20, 20, 30, 40], 40))  # 5
print(first_occurrence([10, 20, 20, 20, 30, 40], 50))  # -1
print(first_occurrence([10, 10, 10, 20, 30], 10))       # 0


# Time Complexity: O(log n)
# Space Complexity: O(1)