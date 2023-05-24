class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # LEETCODE explanation assistance
        count = {}
        sol = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            sol = max(sol, r - l + 1)
        return sol