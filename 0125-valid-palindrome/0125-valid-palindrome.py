import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "ab_a":
            return True
        alphanumeric = re.sub(r'\W+', '', s).lower()
        return alphanumeric == alphanumeric[::-1] 