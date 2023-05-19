class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            i = (l + r) // 2  # Use (l + r) // 2 to calculate the middle index correctly

            if target < nums[i]:
                r = i - 1  # Update r to i - 1 when target is smaller
            elif target > nums[i]:
                l = i + 1  # Update l to i + 1 when target is larger
            else:
                return i  # Return the index if target is found

        return -1  # Return -1 if target is not found
