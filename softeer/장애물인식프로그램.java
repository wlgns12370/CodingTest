import java.io.*;
import java.util.*;

public class Main {
    static int[][] map;
    static Deque<int[]> q;
    static int n;
    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static boolean[][] visited;

    public static int bfsNumbering(int x, int y) {

        q.offer(new int[] {x,y});
        visited[x][y] = true;

        int cnt = 1;
        int cx=0;
        int cy=0;
        int nx=0;
        int ny=0;
        while(!q.isEmpty()) {
            int[] t = q.poll();
            cx = t[0];
            cy = t[1];

            for (int d=0; d < 4; d++){
                nx = cx + dx[d];
                ny = cy + dy[d];
                if (0<= nx && nx < n && 0<= ny && ny<n) {
                    if(map[nx][ny] != 0 && visited[nx][ny] == false) {
                        visited[nx][ny] = true;
                        cnt += 1;
                        q.offer(new int[] {nx,ny});
                    }
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];
        q = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            String line = br.readLine();

            for (int j = 0; j < n; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j] && map[i][j] != 0) {
                    pq.offer(bfsNumbering(i,j));
                }
            }
        }

        System.out.println(pq.size());
        while(!pq.isEmpty()) {
            int a = pq.poll();
            System.out.println(a);
        }
    }
}

