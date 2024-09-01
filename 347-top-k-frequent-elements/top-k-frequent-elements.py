class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements_dict = {}

        for num in nums:
            elements_dict[num] = elements_dict.get(num, 0) + 1
        
        sorted_keys = sorted(elements_dict, key=elements_dict.get, reverse=True)

        return sorted_keys[:k]