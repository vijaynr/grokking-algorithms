# How to find the longest common subsequence between two strings?
# Eg: Given two strings "fish" and "fosh", fsh is common
# sub-sequence between them

def find_common_subsequence(a, b):
    al = len(a)
    bl = len(b)
    max_seq = 0
    cache = [[0 for x in range(bl)] for y in range(al)]
    print(cache)
    for ai in range(0, al):
        for bi in range(0, bl):
            if a[ai] == b[bi]:
                cache[ai][bi] = cache[ai-1][bi-1] + 1
            else:
                cache[ai][bi] = max(cache[ai][bi-1], cache[ai-1][bi])
            max_seq = cache[ai][bi]
    print(max_seq)
    return max_seq


find_common_subsequence("fish", "fishs")