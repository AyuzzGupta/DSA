class Solution {
    public int numIdenticalPairs(int[] nums) {
        int i=0;
        int cnt=0;
        for(int j=0;j<nums.length;j++){
            for(i=0;i<j;i++){
                if (nums[i] == nums[j]){
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
}