class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        print(f"Initial left: {left}, Initial right: {right}")
        while left < right:
            mid = left + (right - left) // 2
            print(f"mid: {mid}")
            hours = sum((pile - 1) // mid + 1 for pile in piles)
            if hours <= h:
                print(f"Current mid: {mid}, Total hours: {hours}, Adjusting right boundary")
                right = mid
            else:
                print(f"Current mid: {mid}, Total hours: {hours}, Adjusting left boundary")
                left = mid + 1

        print(f"Final minimum eating speed: {left}")
        return left
