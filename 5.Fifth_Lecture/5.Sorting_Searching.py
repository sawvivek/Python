# bubble sort

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# arr=[64, 34, 25, 12, 22, 11, 90]
# print("Original array:", arr)

# print("Sorted array:", bubble_sort(arr))

# linear search
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i

# arr = [2, 4, 6, 8, 10]
# target = 5
# result = linear_search(arr, target)
# if result != None:
#     print("Element found at index:", result)
# else:
#     print("Element not found in the array.")
    
# binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
arr = [2, 4, 6, 8, 10]
target = 5
result = binary_search(arr, target)
if result != None:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")