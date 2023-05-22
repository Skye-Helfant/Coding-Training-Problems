class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity: O(n) because iterating through list and set lookups are O(n)
        # Memory Complexity: O(n) 2 * n max, simplifies to O(n)
        
        if not nums:
            return 0

        distinct = set(nums)
        stack = []

        for num in nums:
            if num - 1 not in distinct:
                count = 1
                while num + 1 in distinct:
                    count += 1
                    num = num + 1
                if not stack:
                    stack.append(count)
                if stack and count > stack[-1]:
                    stack.pop()
                    stack.append(count)

        return stack[-1]