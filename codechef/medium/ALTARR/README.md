# ALTARR

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Alternating Array

You have an array $A$ of $N$ integers. You want to make it alternating, i.e. the parity of the elements should keep switching. For example, $[1, 2, 3, 6, 5]$ is valid because it goes Odd, even, odd, even, odd.

Find the minimum changes you need to make to the array to make it valid. Each change is of the form: choose some index $i$, and set $A_i$ to any integer you want.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the minimum changes needed to be made to the array.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le A_i \le 100$
### Sample 1:
Input
Output

```
2
3
1 1 1
3
4 3 6

```

```
1
0

```

### Explanation:

 **Test Case 1:**  You can edit $A_2$ to be $2$, to get $[1, 2, 1]$ and only $1$ change.

 **Test Case 2:**  The given array is already valid.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-15T14:40:43.368Z  

```py
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    changes1 = 0
    for i in range(n):
        if i % 2 == 0:  
            if arr[i] % 2 == 0:
                changes1 += 1
        else: 
            if arr[i] % 2 == 1:
                changes1 += 1
    changes2 = 0
    for i in range(n):
        if i % 2 == 0:  
            if arr[i] % 2 == 1:
                changes2 += 1
        else: 
            if arr[i] % 2 == 0:
                changes2 += 1
    
    print(min(changes1, changes2))

```

---

[View on CodeChef](https://www.codechef.com/problems/ALTARR)