class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x not in s or y not in s:
            return s
        
        count_x = s.count(x)
        count_y = s.count(y)
        middle = ''.join([ch for ch in s if ch != x and ch != y])
        
        return (y * count_y) + middle + (x * count_x)