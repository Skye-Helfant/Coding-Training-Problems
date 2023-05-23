class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        buffer = set()
        length = 0

        while r < len(s):
            if s[r] not in buffer:
                buffer.add(s[r])
                length = max(length, len(buffer))
                r += 1
            else:
                buffer.remove(s[l])
                l += 1

        return length
