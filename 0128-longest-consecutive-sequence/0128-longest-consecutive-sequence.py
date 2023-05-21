class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)

        stack = []

        for num in nums:
            if num - 1 not in distinct:
                temp = 1
                i = 1
                while num + i in distinct:
                    i += 1
                    temp += 1
                if not stack:
                    stack.append(temp)
                if stack and temp > stack[-1]:
                    stack.pop
                    stack.append(temp)

        return stack[-1] if stack else 0