
public class Solution {
    public int ClimbStairs(int n) {
        
        // result is fibbonachi
        
        // initialize array of size n+2 (to account for 0 and 1, fist parts of fib)
        int[] sequence = new int[n+2];
        // set first two parts of fib
        sequence[0] = 0;
        sequence[1] = 1;
        // start at i = 2 to ignore positions 0 and 1
        for (int i = 2; i < n + 2; i++){
            // current = last two entries
            sequence[i] = sequence[i-2] + sequence[i-1];
           
        }
        return sequence[n+1];
        
    }
}