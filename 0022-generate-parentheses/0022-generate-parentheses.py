class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        sol = []

        def backtrack(num_open, num_closed):
            if num_open == num_closed == n:
                sol.append("".join(stack))
                return
            
            if num_open < n:
                stack.append('(')
                backtrack(num_open + 1, num_closed)
                stack.pop()

            if num_closed < num_open:
                stack.append(')')
                backtrack(num_open, num_closed + 1)
                stack.pop()
# Testing Testing
        backtrack(0, 0)
        return sol
                