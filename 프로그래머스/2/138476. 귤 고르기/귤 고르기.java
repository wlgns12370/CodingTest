import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:tangerine) {
            map.put(num, map.getOrDefault(num,0) +1);
        }
        
        PriorityQueue<int[]> countList =
    new PriorityQueue<>((a, b) -> {
        if (a[1] != b[1]) {
            return Integer.compare(b[1], a[1]);
        }
        return Integer.compare(b[0], a[0]);
    });
        
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int num = entry.getKey();
            int count = entry.getValue();
            
            countList.offer(new int[]{num, count});
        }
        
        int answer = 0;
        while(true) {
            if(k <= 0) {
                break;
            }
            
            // max 찾기           
            int[] cur = countList.poll();
            int maxIdx = cur[0];
            int maxCount = cur[1];
            
            // max값 k감소
            k-=maxCount;
            answer++;
        }
        
        return answer;
    }
}