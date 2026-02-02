import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 *
 * N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
 * 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
 *
 * 시간 복잡도 계산
 * 범위 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
 * O(N) -> 10^4
 * 0.5초 -> 15 * 10^8
 *
 * 지식
 * 1초 -> 3GHz -> 3*10^9
 *
 */

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(st.nextToken());
            arr[i] = num;
        }

        int result = 0;
        int start = 0;
        int end = 0;
        int sum = arr[0];
        while(true){
            if(sum < m) {
                end++;
                if(end == n) {
                    break;
                }
                sum += arr[end];
            }
            else if(sum > m) {
                sum -= arr[start];
                start++;
            }
            else if(sum == m) {
                result++;
                end++;
                if(end == n) {
                    break;
                }
                sum += arr[end];
            }
        }
        System.out.println(result);
    }
}
