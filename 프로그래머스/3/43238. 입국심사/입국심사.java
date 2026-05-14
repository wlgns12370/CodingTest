import java.util.Arrays;
class Solution {
    public long ok(long k, long[] times) {
        long temp = 0;
        for(int i = 0; i<times.length; i++) {
            temp += k/times[i];
        }
        return temp;
    }
    public long solution(int n, int[] times) {
        long answer = 0;
        
        long[] times2 = Arrays.stream(times)
                               .mapToLong(i -> (long) i)
                               .toArray();
        long lo = 1;
        long m = times[0];
        for (int time : times) {
            if (time > m) {
                m = time;
            }
        }
        long hi = m*n;
        long mid = 0;
        long num = 0;
        while(lo <= hi) {
            mid = (lo+hi) / 2;
            num = ok(mid, times2);
            if (num < n) {
                lo = mid + 1;
            }
            else {
                answer = mid;
                hi = mid - 1;
            }
        }
        
        return answer;
    }
}