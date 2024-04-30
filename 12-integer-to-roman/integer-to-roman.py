class Solution:
    def intToRoman(self, num: int) -> str:
        # romanNumerals = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thousands = ["","M","MM","MMM"]

        return thousands[num//1000] + hundreds[(num%1000)//100] + tens[(num%100)//10] + ones[int(num%10)]