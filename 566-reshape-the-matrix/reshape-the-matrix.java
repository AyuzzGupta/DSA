class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int[][] nmat=new int[r][c];
        int[] arr=new int[mat.length*mat[0].length];
        int k=0;
        for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[i].length; j++) {
                arr[k]=mat[i][j];
                k++;
            }
        }
        if(mat.length * mat[0].length != r * c){
            return mat;
        }
        else{
            k=0;
            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    nmat[i][j]=arr[k];
                    k++;
            }
        }
        return nmat;
        }
        
    }
}