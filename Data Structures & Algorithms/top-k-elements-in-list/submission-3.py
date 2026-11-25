class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict()
        for x in nums:
            if x in numsDict:
                numsDict[x] += 1
            else:
                numsDict[x] = 0
        return list(sorted(numsDict, key=numsDict.get, reverse=True))[:k]