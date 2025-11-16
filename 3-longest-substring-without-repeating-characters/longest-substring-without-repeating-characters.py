class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == []:
            return 0
        encountered = []
        lengths = []
        for i in s:
            if i in encountered:
                lengths.append(len(encountered))
                index_to_reset = encountered.index(i)
                encountered = encountered[index_to_reset+1:]
                encountered.append(i)
            else:
                encountered += i
        lengths.append(len(encountered))
        return max(lengths)
        