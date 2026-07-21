# TSORT - Rating 667

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Simple Sorting

Given a list of numbers, you have to sort them in non decreasing order.

### Input Format
- The first line contains a single integer, $N$, denoting the number of integers in the list.
- The next $N$ lines contain a single integer each, denoting the elements of the list.
### Output Format

Output $N$ lines, containing one integer each, in non-decreasing order.

### Constraints
- $1 \leq N \leq 10^6$
- $0 \leq$ elements of the list $\leq 10^6$
### Sample 1:
Input
Output

```
5
5
3
6
7
1
```

```
1
3
5
6
7
```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T08:36:54.194Z  

```c_cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    cin >> n;
    
    const int MAX_VALUE = 1000000;
    vector<int> count(MAX_VALUE + 1, 0);
    
    for(int i = 0; i < n; i++) {
        int num;
        cin >> num;
        count[num]++;
    }
    
    for(int i = 0; i <= MAX_VALUE; i++) {
        for(int j = 0; j < count[i]; j++) {
            cout << i << "\n";
        }
    }
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/TSORT)