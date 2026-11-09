class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int ht = bandage[0];
        int hPerSec = bandage[1];
        int plusHeal = bandage[2];
        int n = attacks.length;
        int answer = health;
        
        for(int i = 0; i < n-1; i++){
            // 공격 받고 시간 계산
            answer -= attacks[i][1];
            
            // 죽었으면 -1
            if (answer < 1) {
                return -1;
            }
            
            // 현재 시간과 다음 시간의 차이에 따라 처리
            int t = attacks[i+1][0] - attacks[i][0] -1;
            
            if (t < 1) {
                continue;
            }
            
            int ph = 0;
            if (t >= ht){
                // 체력 더 회복 몫만큼 추가 체력과 시간만큼 초당 회복력
                ph = t/ht;
                
                answer = Math.min(answer+ph*plusHeal+t*hPerSec,health);
            } else {
                answer = Math.min(answer+t*hPerSec,health);
            }
        }
        answer -= attacks[n-1][1];
        if (answer < 1) {
            return -1;
        }
        
        return answer;
    }
}