def sum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return arr[0] + sum(arr[1:n])


def running_sum(arr, sum=0):
    n = len(arr)
    if n == 1:
        return sum + arr[0]
    return running_sum(arr[1:n], sum + arr[0])


print(sum([1, 3, 4, 5]))
print(running_sum([1, 3, 4, 5]))
