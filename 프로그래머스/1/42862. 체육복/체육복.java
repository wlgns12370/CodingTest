import java.util.Arrays;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        int answer = n-lost.length;
        int EXCLUD_STUDENT = -1000;
        
        for(int i=0; i<reserve.length; i++) {
            for(int j=0; j<lost.length; j++) {
                // 자기 자신이 잃어버린 경우
                if(reserve[i] == lost[j]) {
                    reserve[i] = EXCLUD_STUDENT;
                    lost[j] = EXCLUD_STUDENT;
                    answer++;
                    break;
                }
            }
        }
        for(int i=0; i<reserve.length; i++) {
            for(int j=0; j<lost.length; j++) {
                // 자기 왼쪽 사람한테 빌려주는 경우
                if((reserve[i]-1) == lost[j]) {
                    reserve[i] = EXCLUD_STUDENT;
                    lost[j] = EXCLUD_STUDENT;
                    answer++;
                    break;
                }
                // 자기 오른쪽 사람한테 빌려주는 경우
                if((reserve[i]+1) == lost[j]) {
                    reserve[i] = EXCLUD_STUDENT;
                    lost[j] = EXCLUD_STUDENT;
                    answer++;
                }
            }
        }
        
        return answer;
    }
}