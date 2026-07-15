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
    # This is the invariant that must be preserved
    cnt = [0] * k
    for i, ch in enumerate(s):
        if ch == '0':
            cnt[i % k] += 1
    
    # Build the lexicographically smallest string
    ans = ['1'] * n
    placed = 0
    used = [0] * k
    
    # Place zeros as early as possible
    for i in range(n):
        if placed >= zeros:
            break
        
        r = i % k
        # We can place a zero here if we haven't used all
        # the zeros that should be at positions with remainder r
        if used[r] < cnt[r]:
            ans[i] = '0'
            used[r] += 1
            placed += 1
    
    # Place remaining zeros at the end (if any)
    if placed < zeros:
        for i in range(n - 1, -1, -1):
            if placed >= zeros:
                break
            if ans[i] == '1':
                ans[i] = '0'
                placed += 1
    
    print(''.join(ans))