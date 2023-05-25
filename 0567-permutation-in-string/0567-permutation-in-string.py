class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        s1_count = {}
        s2_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        while r <= len(s2):
            s2_count.clear()

            for char in s2[l:r]:
                s2_count[char] = s2_count.get(char, 0) + 1

            if s1_count == s2_count:
                return True

            l += 1
            r += 1

        return False
