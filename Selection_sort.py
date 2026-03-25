def selection_sort(arr):
    n = len(arr)
    min_index = 0
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Sorted array - ", arr)

arr = [64,22,45,12,11]
selection_sort(arr)