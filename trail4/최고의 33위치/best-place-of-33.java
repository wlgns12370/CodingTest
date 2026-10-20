import java.util.Scanner;
public class Main {
    public static void main(String[] args) {

        int[][] d = {
            {0, 0}, {0, 1}, {0, 2},
            {1, 0}, {1, 1}, {1, 2},
            {2, 0}, {2, 1}, {2, 2}
        };

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        
        int ni=0;
        int nj=0;
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                // 검사 코드
                boolean isInner = true;
                int scoreTemp = 0;
                for (int k =0; k<9; k++) {
                    ni = i+d[k][0];
                    nj = j+d[k][1];

                    if (0 > ni || ni >= n || 0 > nj || nj >= n) {
                        isInner = false;
                        break;
                    }
                    scoreTemp += grid[ni][nj];
                }

                if (isInner == true) {
                    if (answer < scoreTemp) {
                        answer = scoreTemp;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}