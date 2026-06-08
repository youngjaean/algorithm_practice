class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        new_arry = [pivot]
        nums.remove(pivot)
        small_index = 0

        for num in nums:
            if num > pivot:
                new_arry.append(num)
            elif num < pivot:
                new_arry.insert(small_index, num)
                small_index += 1
            else:
                new_arry.insert(new_arry.index(pivot), num)

        return new_arry