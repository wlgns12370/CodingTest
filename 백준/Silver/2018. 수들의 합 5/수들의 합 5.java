import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 어떠한 자연수 N은, 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 당신은 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서,
 * 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 알고 싶어한다. 이때, 사용하는 자연수는 N이하여야 한다.
 * 예를 들어, 15를 나타내는 방법은 15, 7+8, 4+5+6, 1+2+3+4+5의 4가지가 있다. 반면에 10을 나타내는 방법은 10, 1+2+3+4의 2가지가 있다.
 * N을 입력받아 가지수를 출력하는 프로그램을 작성하시오.
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());


        if (n == 1) {
            System.out.println(1);
        }
        else if (n == 2) {
            System.out.println(1);
        }
        else if (n == 3) {
            System.out.println(2);
        }
        else {
            int sum = 3;
            int result = 1;

            int lPointer = 1;
            int rPointer = 2;
            while(true) {

                if (lPointer == n-2 && rPointer == n-1) {
                    break;
                }
                if (sum < n) {
                    sum += ++rPointer;
                }
                else if(sum > n) {
                    sum -= lPointer++;
                }
                else if(sum == n) {
                    result++;
                    sum += ++rPointer;
                }
            }
            System.out.println(result);
        }
    }
}
