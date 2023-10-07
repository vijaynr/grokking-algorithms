def find_minimum(arr):
    min = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_idx = i
    return min_idx


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def selection_sort(arr):
    sorted_arr = []
    for i in range(1, len(arr)):
        min_element = find_minimum(arr)
        sorted_arr.append(arr.pop(min_element))
    return sorted_arr


def selection_sort_swap(arr):
    for i in range(0, len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr = swap(arr, i, min_idx)
    return arr


arr = [3, 4, 1, 55, 5, -2, 22]
print(selection_sort_swap(arr))
