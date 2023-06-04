from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_nums = []
        l, r = 0, 0
        queue = deque()
        # print(f"Initial queue: {list(queue)}")

        while r < len(nums):
            # print(f"window: {nums[l:r+1]}, q: {list(queue)}")
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                max_nums.append(nums[queue[0]])
                # print(f"max_num: {nums[queue[0]]}")
                l += 1
            r += 1

        return max_nums
