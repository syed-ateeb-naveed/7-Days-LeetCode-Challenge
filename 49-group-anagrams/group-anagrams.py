class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for word in strs:

            ocurrences = [0] * 26 # [0 ,0 ,0 ,0 ,.....0]

            for letter in word:

                ocurrences[ord(letter)-ord("a")] += 1

            result[tuple(ocurrences)].append(word)
        
        return result.values()