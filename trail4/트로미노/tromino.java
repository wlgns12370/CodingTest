import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] grid = new int[n][m];

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                grid[r][c] = sc.nextInt();
            }
        }

        int[][][] shapes = {
            {{0, 0}, {0, 1}, {1, 0}},
            {{0, 0}, {0, 1}, {1, 1}},
            {{0, 0}, {1, 0}, {1, 1}},
            {{0, 1}, {1, 0}, {1, 1}},
            {{0, 0}, {0, 1}, {0, 2}},
            {{0, 0}, {1, 0}, {2, 0}}
        };

        int answer = 0;

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                for (int s = 0; s < 6; s++) {
                    int sum = 0;
                    boolean valid = true;

                    for (int k = 0; k < 3; k++) {
                        int nr = r + shapes[s][k][0];
                        int nc = c + shapes[s][k][1];

                        if (nr >= n || nc >= m) {
                            valid = false;
                            break;
                        }

                        sum += grid[nr][nc];
                    }

                    if (valid) {
                        answer = Math.max(answer, sum);
                    }
                }
            }
        }

        System.out.println(answer);
    }
}