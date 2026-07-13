# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` *if* `x` *is a   palindrome , and* `false` *otherwise*.

 

 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** C++  
**Runtime:** 5 ms (beats 19.74%)  
**Memory:** 10.9 MB (beats 13.19%)  
**Submitted:** 2026-07-13T09:59:06.171Z  

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        
        string s = to_string(x);
        int n = s.length();
        
        for (int i = 0; i < n / 2; i++) {
            if (s[i] != s[n - 1 - i]) {
                return false;
            }
        }
        
        return true;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)