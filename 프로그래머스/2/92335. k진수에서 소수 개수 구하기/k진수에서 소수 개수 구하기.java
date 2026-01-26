class Solution {
    
    public static String div(int n, int k) {
        StringBuilder sb = new StringBuilder();
        int b = 0; // 나머지
        while(true) {
            
            if (n < k) {
                break;
            }
            b = n%k;
            n = n/k;
            sb.append(b);
        }
        if (n != 0){
            sb.append(n);
        }
        
        return sb.reverse().toString();
    }
    
    public boolean isPrime(long num) {
        if(num < 2) {
            return false;
        }
        if(num == 2) {
            return true;
        }
        boolean flag = true;
        long end = (long)Math.sqrt(num);
        
        for(long i = 2; i<=end; i++) {
            if (num % i == 0) {
                flag=false;
                break;
            }
        }
        return flag;
    }
    
    public int solution(int n, int k) {
        int answer = 0;
        String[] tokens = div(n, k).split("0");
        for(String token : tokens) {
            if (token.equals("")) {
                continue;
            }
            long num = Long.parseLong(token);
            if (isPrime(num)) {
                answer++;
            }
        }
        return answer;
    }
}