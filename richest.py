class Solution:
    def maximumWealth(self, accounts: list[list[int]]):
        self.accounts = accounts
        final_val = []
        for i in range(len(self.accounts)):
            total_wealth = 0
            for j in range(len(self.accounts[i])):
                total_wealth += self.accounts[i][j]
            final_val.append(total_wealth)
        result = max(final_val)
        return result
        
sol = Solution()
accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(sol.maximumWealth(accounts))