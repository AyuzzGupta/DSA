class Solution {
    public int maxDepth(String s) {
        int br=0;
        int max=0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i)=='('){
                br+=1;
            }
                if (br > max) {
                max = br;
                }
            else if (s.charAt(i)==')'){
                br-=1;
            }
        }
        return (max);
    }}