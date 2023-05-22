class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        This method recursively calls backtrack until a string of n * 2 parenthesis has been formed
        It then appends that combination to solution, in the end a list of all possible combinations
        is constructed and returned
        """
        def backtrack(openP, closedP, s):
            if len(s) == n * 2:
                sol.append(s)
                return

            if openP < n:
                backtrack(openP + 1, closedP, s + '(')

            if closedP < openP:
                backtrack(openP, closedP + 1, s + ')')
        
        sol = []
        backtrack(0, 0, '')
        return sol