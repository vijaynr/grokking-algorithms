# Given two strings, find the length of the longest
# common substring that can be formed from it?
# Eg: Sting A - "fish", String B - "issue", Answer - "is" (2)

# naive approach

def find_longest_substring(a, b):
    max_string = ""
    for ai in range(0, len(a)):
        for aj in range(ai, len(a)):
            new_string = a[ai:aj + 1]
            if b.__contains__(new_string):
                if len(new_string) > len(max_string):
                    max_string = new_string
    return max_string


def find_longest_substring2(a, b):
    al = len(a)
    bl = len(b)
    cache = [[0 for x in range(bl)] for y in range(al)]
    max_len = 0
    pos = []
    for ai in range(0, al):
        for bi in range(0, bl):
            if a[ai] == b[bi]:
                cache[ai][bi] = cache[ai - 1][bi - 1] + 1
                if cache[ai][bi] > max_len:
                    max_len = cache[ai][bi]
                    pos = [ai, bi]
    common_str = ["" for x in range(max_len)]
    ai = pos[0]
    bi = pos[1]
    it = max_len - 1
    start = cache[ai][bi]
    while start != 0:
        common_str[it] = a[ai]
        ai -= 1
        bi -= 1
        it -= 1
        start = cache[ai][bi]
    print("".join(common_str))
    return


find_longest_substring2("bbblue", "cluesbbbl")
