class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == "".join(reversed(str(x))):
            print(sorted(str(x)))
            return True
        else:
            print("".join(reversed(sorted(str(x)))))
            return False
