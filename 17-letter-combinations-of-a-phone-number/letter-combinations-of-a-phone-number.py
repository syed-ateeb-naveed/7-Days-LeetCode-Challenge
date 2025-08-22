from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],
                   5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'],
                   8:['t','u','v'], 9:['w','x','y','z']}

        if digits == "":
            return [] 
        result = list(product(*[buttons[int(i)] for i in digits]))
      
        joined = ["".join(pair) for pair in result]

        print(joined)

        return joined