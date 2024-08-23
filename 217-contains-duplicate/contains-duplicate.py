class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d.keys():
                return True
            d[num] = 1
        return False