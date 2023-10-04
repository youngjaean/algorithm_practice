class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while len(numbers) >= i:
            value = numbers[i]
            mod = target - value
            if mod in numbers:
                answer = numbers.index(mod)
                if i != answer:
                    return sorted([i + 1, answer + 1])
                else:
                    i += 1
            else:
                i += 1

        else:
            return []