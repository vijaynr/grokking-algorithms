def count_list(arr):
    def next_element(count=0):
        try:
            count = count + 1
            return next_element(count)
        except IndexError:
            return count

    return next_element()


print(count_list([1, 4, 5, 6, 7, 7]))