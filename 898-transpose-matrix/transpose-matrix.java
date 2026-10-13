class Solution {
    public int[][] transpose(int[][] matrix) {
        int rows = matrix.length;       // 2
        int cols = matrix[0].length;    // 3
        int[][] newMatrix = new int[cols][rows];
        for(int i=0;i<cols;i++){
            for(int j=0;j<rows;j++){
                newMatrix[i][j]=matrix[j][i];
            }
        }
        return newMatrix;
    }
}