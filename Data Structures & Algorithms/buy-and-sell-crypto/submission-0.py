class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #the buying < selling
        #buying happens before selling
        #min(buying) and max(selling) => max profit else 0
        profit=0
        mini=prices[0]
        for i in range(len(prices)-1):
              j=i+1
              mini=min(mini,prices[i])
              temp=prices[j]-mini
              profit=max(profit,temp)
        return profit  

        