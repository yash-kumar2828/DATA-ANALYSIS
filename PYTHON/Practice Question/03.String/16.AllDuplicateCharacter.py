'''Print All Duplicate Characters with Counts
Input: sinstriiintng
Output: i:4, n:3, s:2, t:2   '''


def get_duplicate_character(str1):

    d = {}

    for i in str1:
        d[i] = d.get(i,0)+1

    res = []
    for i in sorted(d):
        if d[i]>1:
            res.append(f"{i}:{d[i]}")

    if len(res) == 0 :
        print(res)

    else:
        output = ", ".join(res)
        print(output)


str1 = input('Enter the string : ')
get_duplicate_character(str1)
