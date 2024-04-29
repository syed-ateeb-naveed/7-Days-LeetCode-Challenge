class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sentence = s.strip()
        words = sentence.split()
        return len(words[-1])