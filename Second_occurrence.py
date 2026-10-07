arr = [2, 4, 4, 4, 6, 8, 10]
target = 4

count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1
        if count == 2:
            print("Second occurrence:", i)
            break