class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]

        for i in range(1, len(strs)):

            while strs[i][:len(first)] != first:
                first = first[:-1]
                if first == "":
                    break

        return first