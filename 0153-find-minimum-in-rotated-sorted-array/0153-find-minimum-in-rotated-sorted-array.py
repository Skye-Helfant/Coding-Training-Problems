class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = nums[0] # initialize solution
        l, r = 0, len(nums) - 1 # Initialize left and right pointers

        while l <= r:
            if nums[l] < nums[r]:
                sol = min(sol, nums[l]) # Found kink break uut
                break

            m = (l + r) // 2
            sol = min(sol, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return sol