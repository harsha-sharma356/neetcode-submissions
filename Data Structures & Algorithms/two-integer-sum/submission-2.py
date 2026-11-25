class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = {}
        for i, n in enumerate(nums):
            if target-n in out:
                return [out[target-n], i]
            out[n] = i