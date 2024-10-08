class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1 

        while lo < hi:
            sumi = numbers[lo] + numbers[hi]

            if sumi == target:
                return [lo + 1, hi + 1]
            elif sumi < target:
                lo += 1
            else:
                hi -= 1
        return [-1, -1]