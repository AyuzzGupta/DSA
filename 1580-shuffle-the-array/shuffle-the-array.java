class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] x= new int[n];
        int[] y=new int[n];
        int[] shuf=new int[2*n];
        int xi=0;
        for(int i=0;i<2*n;i++){
            if (i<n){
                x[i]=nums[i];
            }
            else{
                y[xi]=nums[i];
                xi++;
            }
        }
        xi=0;
        int yi=0;
        for(int i=0;i<2*n;i++){
            if (i%2!=0){
                shuf[i] =y[yi];
                yi++;
                // shuf[i] =x[xi];
                // xi++;
            }
            else{
                // shuf[i] =y[yi];
                // yi++;
                shuf[i] =x[xi];
                xi++;
            }
        }
        return shuf;
    }
}