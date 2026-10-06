arr = [2, 4, 6, 4, 8, 4, 10]
target = 4

left = 0
right = len(arr) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        ans = mid
        left = mid + 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print("Last occurrence:", ans)