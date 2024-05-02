class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        for i in range(len(bank)):
            if i == len(bank) - 1:
                break
            ones_above = bank[i].count("1")
            if int(ones_above): 
                for j in range(i+1, len(bank)):
                    if "1" in bank[j]:
                        beams += ones_above * int(bank[j].count("1"))
                        break
        
        return beams
