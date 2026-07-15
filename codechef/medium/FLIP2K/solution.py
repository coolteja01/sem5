t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    zeros = s.count('0')
    ones = n - zeros
    
    # If we can't perform even one operation
    if zeros < k or ones < k:
        print(s)
        continue
    
    # Count zeros at each position modulo k
    # This invariant must be preserved EXACTLY
    cnt = [0] * k
    for i, ch in enumerate(s):
        if ch == '0':
            cnt[i % k] += 1
    
    # Build the lexicographically smallest string
    ans = ['1'] * n
    used = [0] * k
    
    # Place zeros as early as possible
    # We must place exactly cnt[r] zeros at positions
    # where i % k == r, for each r
    for i in range(n):
        r = i % k
        if used[r] < cnt[r]:
            ans[i] = '0'
            used[r] += 1
    
    print(''.join(ans))