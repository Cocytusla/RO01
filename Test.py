#冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))

# Path: Test.py
#插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))

# Path: Test.py
#选择排序
def selection_sort(arr):
    for i in range (len(arr)):
         min_idx = i
         for j in range(i+1, len(arr)):
             if arr[min_idx] > arr[j]:
                 min_idx = j
         arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))


