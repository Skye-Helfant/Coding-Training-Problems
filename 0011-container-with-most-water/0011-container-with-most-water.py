class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        def compute_area(left, right) -> int:
            # returns water area
            if height[left] > height[right]:
                return height[right] * (right-left)
            else:
                return height[left] * (right-left)

        while right > left:
            area = compute_area(left, right)
            max_area = max(max_area, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
