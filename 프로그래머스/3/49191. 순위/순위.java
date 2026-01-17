class Solution {
    
    static boolean[][] winTable;
    
    public int solution(int n, int[][] results) {
        
        winTable = new boolean[n+1][n+1];
        
        for(int[] node : results) {
            winTable[node[0]][node[1]] = true;
        }
        
        for(int k=1; k<=n; k++) {
            for(int i=1; i<=n; i++) {
                for(int j=1; j<=n; j++) {
                    if(winTable[i][k] && winTable[k][j]) {
                        winTable[i][j] = true;
                    }
                }
            }
        }
        
        int answer = 0;
        // indegree outdegree 개수 파악
        for(int i=1; i<=n; i++) {
            int indegree = 0;
            int outdegree = 0;
            
            // winTable[i][?] -> i번 노드가 이긴 것
            // winTable[?][i] -> i번 노드가 진 것
            
            for(int k =1; k<=n; k++) {
                if (winTable[i][k]) outdegree++;
                if (winTable[k][i]) indegree++;
            }
            if(indegree + outdegree == n-1) {
                answer++;
            }
        }
        
        return answer;
    }
}