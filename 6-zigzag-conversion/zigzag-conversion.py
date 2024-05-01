
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)

        if numRows < 2:
            return s

        i = 0

        converted = ""

        while i < numRows:
            idx = i
            while idx < n:
                converted+=s[idx]
                if idx%(numRows-1) != 0:
                    diff = ((numRows-1) - idx%(numRows-1))*2
                    if idx+diff >= n:
                        break
                    converted+=s[idx+diff]
                idx+=(numRows-1)*2
            i+=1
        return converted
        