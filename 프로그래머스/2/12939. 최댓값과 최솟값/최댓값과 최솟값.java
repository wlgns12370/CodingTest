import java.util.*;

class Solution {
    public String solution(String s) {
        
        StringTokenizer st = new StringTokenizer(s, " ");
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        while(st.hasMoreTokens())
        {
            int value = Integer.valueOf(st.nextToken());
            
            if (min > value) {
                min = value;
            }
            if (max < value) {
                max = value;
            }
        }
        String answer = min + " " + max;
        return answer;
    }
}