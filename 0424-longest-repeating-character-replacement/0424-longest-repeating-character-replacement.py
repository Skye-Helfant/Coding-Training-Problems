class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        sol = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # print("Window: ", s[l:r+1])
            # print("Count: ", count)
            # print("Max Count: ", max(count.values()))
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                # print("Shrinking window...")
                # print("Window: ", s[l:r+1])
                # print("Count: ", count)
                # print("Max Count: ", max(count.values()))
            
            sol = max(sol, r - l + 1)
            # print("Current longest substring length: ", sol)
            # print("-------------------")
        
        return sol
