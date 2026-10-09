class Solution {
    public int heightChecker(int[] heights) {
        int[] expected =heights.clone(); 
        int temp;
        int cnt=0;
        int mini=heights[0];
        for(int i =heights.length-1;i>=0;i--){
            for(int j=0;j<i;j++){
                if(heights[j]>heights[j+1]){
                    temp=heights[j+1];
                    heights[j+1]=heights[j];
                    heights[j]=temp;
                }
            }
        }
        for(int i=0;i<heights.length;i++){
            if (heights[i]!=expected[i]){
                cnt++;
            }
        }
        return cnt;
    }
}