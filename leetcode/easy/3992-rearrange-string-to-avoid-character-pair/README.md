# Rearrange String to Avoid Character Pair

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given a string `s` and two distinct lowercase English letters `x` and `y`.

Rearrange the characters of `s` to construct a new string `t` such that:

- t is a permutation of s.
- Every occurrence of y appears before every occurrence of x in t.

Return any valid string `t`.

 

 **Example 1:** 

 **Input:**  s = "aabc", x = "a", y = "c"

 **Output:**  "cbaa"

 **Explanation:** 

The string `"cbaa"` is a permutation of `"aabc"`, and every occurrence of `'c'` appears before every occurrence of `'a'`.

 **Example 2:** 

 **Input:**  s = "dcab", x = "d", y = "b"

 **Output:**  "cabd"

 **Explanation:** 

The string `"cabd"` is a permutation of `"dcab"`, and every occurrence of `'b'` appears before every occurrence of `'d'`.

 **Example 3:** 

 **Input:**  s = "axe", x = "o", y = "x"

 **Output:**  "axe"

 **Explanation:** 

The string `"axe"` is already valid. Since `'o'` does not occur in the string, the required condition is automatically satisfied.

 

 **Constraints:** 

- 1 <= s.length <= 100
- s consists of lowercase English letters.
- x and y are lowercase English letters.
- x != y

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 76.46%)  
**Submitted:** 2026-07-21T05:26:30.151Z  

```py
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x not in s or y not in s:
            return s
        
        count_x = s.count(x)
        count_y = s.count(y)
        middle = ''.join([ch for ch in s if ch != x and ch != y])
        
        return (y * count_y) + middle + (x * count_x)
```

---

[View on LeetCode](https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/)