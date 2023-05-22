class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                print(f"Target ({target}) is less than the first element in row {row}")
                bot = row - 1
            elif target > matrix[row][-1]:
                print(f"Target ({target}) is greater than the last element in row {row}")
                top = row + 1
            else:
                print(f"Target ({target}) is within the range of row {row}")
                break

        if not (top <= bot):
            print("Target is not found in any row")
            return False
        
        row = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                print(f"Target ({target}) is greater than element at index {m} in row {row}")
                l = m + 1
            elif target < matrix[row][m]:
                print(f"Target ({target}) is less than element at index {m} in row {row}")
                r = m - 1
            else:
                print(f"Target ({target}) is found at index {m} in row {row}")
                return True
