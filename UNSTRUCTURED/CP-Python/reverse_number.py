def reverse_num(n):
    s = str(n)
    rev = ""
    for i in range(len(s)-1, -1, -1):
        rev += s[i]

    return int(rev)

T = int(input())
for i in range(T):
    n = int(input())
    print(reverse_num(n))