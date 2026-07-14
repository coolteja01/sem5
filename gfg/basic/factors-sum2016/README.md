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

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-14T09:22:27.606Z  

```cpp
class Solution {
  public:
    long long factorSum(int N) {
        if (N == 1) return 1;
        
        long long sum = 1;
        int temp = N;
        
        for (int p = 2; p * p <= temp; p++) {
            if (temp % p == 0) {
                int count = 0;
                long long power = 1;
                while (temp % p == 0) {
                    temp /= p;
                    count++;
                    power *= p;
                }
                sum *= (power * p - 1) / (p - 1);
            }
        }
        
        if (temp > 1) {
            sum *= (1 + temp);
        }
        
        return sum;
    }
};
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/factors-sum2016/1)