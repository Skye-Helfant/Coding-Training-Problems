class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = 1
        temp = pointer_1

        while target != (numbers[pointer_1] + numbers[pointer_2]):
            if pointer_2 == len(numbers) - 1 or (numbers[pointer_1] + numbers[pointer_2]) > target:
                while numbers[pointer_1] == numbers[temp]:
                    pointer_1 += 1
                temp = pointer_1
                pointer_2 = pointer_1 + 1
            elif pointer_2 < len(numbers) - 1:
                pointer_2 += 1

        return [pointer_1 + 1, pointer_2 + 1]
        