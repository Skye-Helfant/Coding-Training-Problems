class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[pos, speed] for pos, speed in zip(position, speed)]

        stack = []
        for pos, speed in sorted(pos_speed)[::-1]:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)