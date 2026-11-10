import java.util.*;
class Solution {
    
    int[] m;
    String[][] p;
    int n;
    int n2;
    
    public boolean isOk(int mat, int x, int y) {
        boolean isOk = true;
        for(int i = x; i < x+mat; i++) {
            for (int j = y; j < y+mat; j++) {
                if (!(0 <= i && i< n && 0<= j && j < n2)) {
                    isOk = false;
                    return isOk;
                }
                
                if (!p[i][j].equals("-1")) {
                    isOk = false;
                    return isOk;
                }
            }
        }
        return isOk;
    }
    
    public int solution(int[] mats, String[][] park) {
        m = mats;
        p = park;
        n = park.length;
        n2 = park[0].length;
        
        int answer = -1;
        
        for(int k = 0; k < mats.length; k++) {
            boolean isPut = false;
            for (int i = 0; i<n; i++) {
                for (int j = 0; j < n2; j++) {
                    // 돗자리를 놓을 수 있는 경우
                    if (park[i][j].equals("-1")) {
                        if(isOk(mats[k],i,j)) {
                            answer = Math.max(answer, mats[k]);
                        }
                    }
                }
                if(isPut == true) {
                    break;
                }
            }
        }
        
        return answer;
    }
}