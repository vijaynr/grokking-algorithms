def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while True:
        if low >= len(arr) or high <= 0:
            return None
        mid = (high + low) // 2
        guess = arr[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid

def binary_search_rec(arr, item):
    low = 0
    high = len(arr) - 1

    def _binary_search(arr, low, high):
        if low >= len(arr) or high <= 0:
            return None
        mid = (high + low) // 2
        guess = arr[mid]
        if guess > item:
            high = mid - 1
        if guess < item:
            low = mid + 1
        if guess == item:
            return mid
        return _binary_search(arr, low, high)

    return _binary_search(arr, low, high)


arr = [1, 3, 4, 5, 6, 7]
print(binary_search(arr, 4))

