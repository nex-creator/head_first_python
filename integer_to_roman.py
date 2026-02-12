class Solution:
    def intToRoman(self, num: int) -> str:
        roman_values =""
        values = [(1000,"M"),
                  (900,"CM"),
                  (500,"D"),
                  (400,"CD"),
                  (100,"C"),
                  (90,"XC"),
                  (50,"L"),
                  (40,"XL"),
                  (10,"X"),
                  (9,"IX"),
                  (5,"V"),
                  (4,"IV"),
                  (1,"I")]
        for value in values:
            while num >= value[0]:
                roman_values = roman_values + value[1]
                num = num - value[0]
        return(roman_values)
sol = Solution()
print(sol.intToRoman(58))


        
        







