
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    start = -1
    for i in range(n):
        if s[i] != 'a':
            start = i
            break
    
    if start == -1:
        s[-1] = 'b'
    else:
        i = start
        while i < n and s[i] != 'a':
            s[i] = chr(ord(s[i]) + 1)
            i += 1
    
    print(''.join(s))