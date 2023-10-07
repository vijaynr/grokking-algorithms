
def frequency_count(arr):
    freq_dict = {}
    for item in arr:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict


freq = frequency_count([1, 2, 3, 4, 5, 5, 6, 6, 1, 1, 1])
print(freq[6])
