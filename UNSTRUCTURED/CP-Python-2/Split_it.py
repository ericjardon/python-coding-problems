
def split_it(S, n, k):
    n_segments = 2*k + 1
    if n_segments > n:
        print("NO")
        return

    # find k segments
    count = 0
    i = 0
    while i<n:
        if count==k: break
        if (S[i] != S[n-1-i]): # segment ok, split
            print("NO")
            return
        else:
            count +=1
        i += 1
    print("YES")

for t in range(int(input())):
    n, k = [int(x) for x in input().split()]
    S = input()
    split_it(S, n, k)