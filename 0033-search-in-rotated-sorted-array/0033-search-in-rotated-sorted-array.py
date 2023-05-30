class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            print("The list is empty.")
            return -1

        l, r = 0, len(nums) - 1

        if nums[r] == target:
            return r

        if nums[l] == target:
            return l
        print("The left pointer is at", l)
        print("The right pointer is at", r)

        while nums[l] > nums[r] and target < nums[r]:
            print("The list is reversed. Moving the right pointer to the left.")
            l += 1

        print("The left pointer is at", l)
        print("The right pointer is at", r)

        while nums[l] > nums[r] and target > nums[l]:
            print("The list is reversed. Moving the left pointer to the right.")
            r -= 1

        print("The left pointer is at", l)
        print("The right pointer is at", r)

        while l <= r:
            m = (r + l) // 2
            print("The middle element is", nums[m])
            if target < nums[m]:
                print("The target is smaller than the middle element. Moving the right pointer to the left.")
                r = m - 1
            elif target > nums[m]:
                print("The target is larger than the middle element. Moving the left pointer to the right.")
                l = m + 1
            else:
                print("The target is equal to the middle element. Returning the index.")
                return m
        return -1
