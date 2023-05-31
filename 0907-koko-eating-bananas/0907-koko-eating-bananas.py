class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles, speed, h):
            print("Checking if it is possible to finish all the piles in {} seconds with a speed of {}".format(h, speed))
            time = 0
            for pile in piles:
                time += -(-pile // speed)  # Equivalent to ceil(pile / speed)
                if time > h:
                    print("It is not possible to finish all the piles in {} seconds with a speed of {}".format(h, speed))
                    return False
            print("It is possible to finish all the piles in {} seconds with a speed of {}".format(h, speed))
            return True
        
        print("Finding the minimum eating speed...")
        start = 1
        end = max(piles)

        while start < end:
            mid = start + (end - start) // 2
            print("Checking if it is possible to finish all the piles in {} seconds with a speed of {}".format(h, mid))
            if can_finish(piles, mid, h):
                end = mid
            else:
                start = mid + 1

        print("The minimum eating speed is {}".format(start))
        return start
