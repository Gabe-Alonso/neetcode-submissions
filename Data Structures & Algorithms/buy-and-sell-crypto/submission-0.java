class Solution {
    public int maxProfit(int[] prices) {
        int buy = 0;
        int max_profit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < prices[buy]){
                buy = i;
            }
            if (prices[i] - prices[buy] > max_profit){
                max_profit = prices[i] - prices[buy];
            }
        }
        
        return max_profit;
    }
}
