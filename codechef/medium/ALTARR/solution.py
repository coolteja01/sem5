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
