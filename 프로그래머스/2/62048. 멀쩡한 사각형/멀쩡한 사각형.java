class Solution {
    public long solution(int w, int h) {
        int g = gcd(w, h);

        return (long) w * h - ((long) w + h - g);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int remainder = a % b;
            a = b;
            b = remainder;
        }
        return a;
    }
}