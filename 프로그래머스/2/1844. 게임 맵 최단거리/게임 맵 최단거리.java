import java.util.*;
class Solution {
    static int[] dx = new int[]{0,1,0,-1};
    static int[] dy = new int[]{1,0,-1,0};
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        int[][] visited = new int[n][m];
        
        Deque<int[]> q = new ArrayDeque<>();
        visited[0][0] = 1;
        q.offer(new int[] {0,0});
        int x;
        int y;
        int nx;
        int ny;
        while(!q.isEmpty()) {
            int[] t = q.poll();
            x = t[0];
            y = t[1];
            
            for(int i = 0; i < 4; i++) {
                nx = x + dx[i];
                ny = y + dy[i];
                
                if (0<= nx && nx < n && 0<= ny && ny < m && maps[nx][ny] == 1) {
                    if(visited[nx][ny] == 0) {
                        visited[nx][ny] = visited[x][y] + 1;
                        q.offer(new int[]{nx,ny});
                    }
                }
            }
        }
        
        return (visited[n-1][m-1] != 0) ? visited[n-1][m-1] : -1;
    }
}