import java.util.Scanner;
  
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        
        int answer = 0;
        // 동일원소 파악 방법
        // 세로 파악 파트
        // 0 row 순회 아래쪽으로 쭉 0~[][i]로 순회해서 이전과 다른 값이 나오면 리셋
        // 뒤에 같은 값이 나오면 temp 계속 올림

        for (int i=0; i<n; i++){
            int temp = 1;
            int[] length = new int [n];
            int idx = 0;
            for (int j=1; j<n; j++) {
                if (grid[j][i] == grid[j-1][i]) {
                    temp+=1;
                }
                else {
                    temp = 1;
                }

                if (temp >= m) {
                    break;
                }
            }
            if (temp >= m) {
                answer+=1;
            }
        }

        for (int i=0; i<n; i++){
            int temp = 1;
            int[] length = new int [n];
            int idx = 0;
            for (int j=1; j<n; j++) {
                if (grid[i][j] == grid[i][j-1]) {
                    temp+=1;
                }
                else {
                    temp = 1;
                }

                if (temp >= m) {
                    break;
                }
            }
            if (temp >= m) {
                answer+=1;
            }
        }

        System.out.println(answer);
        
    }
}