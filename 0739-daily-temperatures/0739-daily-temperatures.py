class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                answers[stackIndex] = (i - stackIndex)
            stack.append([i, t])
        return answers