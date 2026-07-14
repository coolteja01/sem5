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