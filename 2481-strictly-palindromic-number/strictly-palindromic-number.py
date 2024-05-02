class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def to_base_n(num, base):
            if num == 0:
                return '0'
            digits = []
            while num:
                digits.append(str(num % base))
                num //= base
            return ''.join(digits[::-1])

        for i in range(2, n-1):
            converted_string = to_base_n(n, i)
            reversed_string = converted_string[::-1]
            if converted_string != reversed_string:
                return False
        
        return True