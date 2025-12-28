import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static long[] arr;
    static long M;

    static boolean check(long num) {
        long temp = 0;
        for (long data : arr) {
            if (data > num) {
                temp += (data-num);
            }
        }

        return temp >= M;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        M = Long.parseLong(st.nextToken());

        arr = new long[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            long num = Long.parseLong(st.nextToken());
            arr[i] = num;
        }

        long lo = 0;
        long hi = 1000000000;
        long mid;

        while (lo + 1 < hi) {
            mid = (lo + hi) / 2;
            if (check(mid)) {
                lo = mid;
            } else {
                hi = mid;
            }
        }

        System.out.println(lo);
    }
}
