class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1;
        int zero_count = 0;
        int[] sol = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                zero_count += 1;
            }else{
                product = product * nums[i];
            }
        }

        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 0){
                if (zero_count > 1){
                    sol[i] = 0;
                }else{
                    sol[i] = product;
                }
            }else{
                if (zero_count > 0){
                    sol[i] = 0;
                }else{
                    sol[i] = product / nums[i];
                }
            }
        }

        return sol;
        
    }
}  
