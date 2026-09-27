class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] newArr = new int[nums.length*2];
        int n=1;
        int j=0;
        while (n<=2){
            for(int i=0;i<nums.length;i++){
                newArr[j]=nums[i];
                j++;
            }
            n=n+1;
        }
        return newArr;
    }
}