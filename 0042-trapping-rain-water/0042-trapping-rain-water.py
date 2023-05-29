class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0

        l, r = 0, length - 1
        left_max, right_max = height[l], height[r]
        sol = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                sol += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                sol += right_max - height[r]

        return sol