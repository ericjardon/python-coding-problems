'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
DO NOT USE libraries or convert to ints
'''


# its Basically the arith problem.

def multiply(num1: str, num2: str) -> str:
        # 1. Pick the larger on in terms of digits
        top = num1 if len(num1) > len(num2) else num2
        bottom = num1 if top==num2 else num2
        print("top", top)
        print("bottom", bottom)
        # 2. IMPORTANT: reverse both strings so positions are read rtl in indexes 0..N
        top = top[::-1]
        bottom = bottom[::-1]
        subproducts = []  # subproducts
        offset = 0
        # 3. Generate subproducts of multplying top with every digit of bottom as int arrays
        # For every digit of bottom
        for i in range(len(bottom)):
            # Multiply with every digit of top
            temp = [0 for _ in range(len(top)+offset)]  # subproduct length is at least same as top, plus zeroes
            carry = 0
            for j in range(len(top)):
                #print(top[j],"x",bottom[i],"=", int(top[j]) * int(bottom[i]))
                
                p = int(top[j]) * int(bottom[i]) + carry
                #print("  + ", carry)
                #print("  ",p)
                carry, digit = divmod(p, 10)
                temp[i+j] = digit
            if carry > 0:
                temp.append(carry)
            subproducts.append(temp)
            offset += 1
        
        # 4. Add up subproducts columnwise
        ans = []  
        carry = 0

        for i in range(len(subproducts[-1])):
            column = [sp[i] for sp in subproducts if len(sp) > i]
            val = sum(column) + carry
            carry, digit = divmod(val, 10)
            ans.append(digit)

        if carry > 0:
            ans.append(carry)
        
        # 5. reverse and convert to string
        ans = ''.join([str(x) for x in ans[::-1]])
        start_i = 0
        while ans[start_i] == '0' and start_i < len(ans)-1:
            start_i += 1

        return ans[start_i:]
        # Integer array to be returned as a reversed string


print(multiply("9133", "0"))         

# let = [[1,9,9,8], [0,1,9,9,8]]
# ans = []  
# carry = 0
# for i in range(len(let[-1])):
#     column = [sp[i] for sp in let if len(sp) > i]
#     val = sum(column) + carry
#     carry, digit = divmod(val, 10)
#     ans.append(digit)
# if carry > 0:
#     ans.append(carry)
# print([''.join([str(x) for x in ans[::-1]])]) 

