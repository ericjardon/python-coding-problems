# INTEGERS IN PYTHON ARE UNBOUNDED.
# SO THERE IS NO RISK OF OVERFLOW 

def superDigit(n, k):
    # We do not need to actually multiply n by k
    # the super digit of '22' is 4, and '22'+'22' is 8. All we do is multiply sd(n)*k

    def sdigit(num):
        # Recurse until num is a single digit
        if num < 10:
            return num
        s = sum([int(x) for x in str(num)])
        return sdigit(s)

    res = sdigit(int(n)) * k
    # Again find the superdigit of the preliminar result
    return sdigit(res)

  
if __name__=="__main__":
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)



### WRONG APPROACH
def _superDigit(n, k):
    # String formed is too long to be efficient
    x = ""
    for _ in range(k):
        x += n
    
    def sd(num): 
        if len(num)==1:
            return int(num)
        
        s=0
        for n in num:
            s += int(n)
        
        return sd(str(s))
    
    return sd(x)