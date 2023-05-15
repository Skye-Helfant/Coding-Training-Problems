class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left, middle, right = 0, 1, len(nums) - 1
        triplets = []

        while left < len(nums) - 2:
            s = nums[left] + nums[middle] + nums[right]
            if s == 0:
                triplets.append([nums[left], nums[middle], nums[right]])
                # Skip over all duplicates of left, middle, and right
                while left < len(nums) - 2 and nums[left] == nums[left+1]:
                    left += 1
                while middle < right and nums[middle] == nums[middle+1]:
                    middle += 1
                while middle < right and nums[right] == nums[right-1]:
                    right -= 1
                # Move middle and right pointers
                middle += 1
                right -= 1
            elif s > 0:
                right -= 1
            else:
                middle += 1
            if middle >= right or right >= len(nums):
                left += 1
                middle = left + 1
                right = len(nums) - 1

        return triplets
