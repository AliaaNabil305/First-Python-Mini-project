# Input array
arr = [38, 27, 43, 3, 9, 82, 10]
n = len(arr)

size = 1 
while size < n:
    for i in range(0, n, size * 2):  
        left = arr[i:i + size] 
        right = arr[i + size:i + size * 2] 
        li = ri = 0
        merged = []
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                merged.append(left[li])
                li += 1
            else:
                merged.append(right[ri])
                ri += 1

        while li < len(left):
            merged.append(left[li])
            li += 1
        while ri < len(right):
            merged.append(right[ri])
            ri += 1
        arr[i:i + len(merged)] = merged
    size *= 2 

print("Sorted Array:", arr)
