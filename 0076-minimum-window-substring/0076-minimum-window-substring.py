from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        output = ""
        l = 0
        t_count = defaultdict(int)
        s_count = defaultdict(int)

        for char in t:
            t_count[char] += 1

        r = l
        while r < len(s):
            s_count[s[r]] += 1
            
            while all(s_count[char] >= t_count[char] for char in t_count):
                if output == "" or len(output) > r - l + 1:
                    output = s[l:r+1]
                
                s_count[s[l]] -= 1
                l += 1

            r += 1

        return output
