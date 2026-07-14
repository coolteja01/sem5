# Factors Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **N**, find the sum of all its factors.

 **Example 1:** 

```
Input: N = 30
Output: 72
Explanation: Factors sum 1 + 2 + 3 + 5 
+ 6 + 10 + 15 + 30 = 72
```

 **Example 2:** 

```
Input: N = 15
Output: 24
Explanation: Factors sum 1 + 3 + 5 
+ 15 = 24
```

 **Your Task:** 
You don't need to read input or print anything. Your task is to complete the function  **factorSum()**  which takes N as input and returns the sum.

 **Expected Time Complexity:**  O(sqrt N)
 **Expected Auxiliary Space:**  O(1)

 **Constraints:** 
1 ≤  **N** ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-14T09:22:49.065Z  

```py
class Solution:
    def factorSum(self, N):
        if N == 1:
            return 1
        
        total_sum = 1
        temp = N
        p = 2
        
        while p * p <= temp:
            if temp % p == 0:
                count = 0
                while temp % p == 0:
                    temp //= p
                    count += 1
                total_sum *= (p ** (count + 1) - 1) // (p - 1)
            p += 1 if p == 2 else 2  # 2, then 3, 5, 7...
        
        if temp > 1:
            total_sum *= (1 + temp)
        
        return total_sum  
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/factors-sum2016/1)