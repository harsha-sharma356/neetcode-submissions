class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = list(map(lambda x: target - x, nums))
        out = []
        for i in range(len(nums)):
            for j in range(len(nums)):     
                if i != j and i not in out and j not in out:
                    if nums[i] + nums[j] == target:
                        out.append(i)
                        out.append(j)
        return out