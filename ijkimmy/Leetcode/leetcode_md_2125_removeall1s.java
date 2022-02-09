package RecSys_3_Algorithm.ijkimmy.Leetcode;

public class leetcode_md_2125_removeall1s {
    // input:   m x n matrix
    // output:  boolean
    // problem: 
    // In one operation, you can choose any row or column and flip each value
    // in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
    // Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

    // Q
    // range of n, m    1<=m,n<=300
    // valid input?     O

    // Solution
    // logic: after flipping 1s in first row w/ col-wise flips, the only operation it can then perform is row-wise flip
    // 1. Naive approach, time: O(mn), space: O(1)
    //      Iterate thru the first row
    //          If cell contains 1, flip entire col
    //      Iterate thru grid
    //          If row has mix of 1s & 0s, return false
    //      return true

    // 33m
    public boolean removeOnes(int[][] grid) {
        for(int c=0; c<grid[0].length; ++c)
            if(grid[0][c] == 1)
                for(int r=0; r<grid.length; ++r)
                    grid[r][c] = -grid[r][c] + 1;
        
        for(int r=1; r<grid.length; ++r)
            for(int c=1; c<grid[r].length; ++c)
                if(grid[r][c] != grid[r][c-1])
                    return false;

        return true;
    }
}