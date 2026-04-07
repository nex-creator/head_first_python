class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        count = 0

        # skip trailing spaces
        while i >= 0 and s[i] ==" ":
            i -= 1

        #count the last word
        while i >=0 and s[i] != " ":
            count +=1
            i -= 1
        return count


sol = Solution()
print(sol.lengthOfLastWord("go to tehe moonnnn"))
