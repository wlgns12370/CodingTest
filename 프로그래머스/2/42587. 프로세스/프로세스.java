import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        
        // pq로 뽑는 순위 관리 deque으로 스케쥴링
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        
        for (int i = 0; i < priorities.length; i++) {
            pq.offer(priorities[i]);
        }
        //[1,2],[2,1][3,3][4,2]
        Deque<int[]> q = new ArrayDeque<>();
        // List<int[]> list = new ArrayList<>(); 
        for (int i = 0; i < priorities.length; i++) {       
            q.offer(new int[]{i,priorities[i]}); // new int[] {}
        }
        
        int[] temp = new int[priorities.length];
        int idx = 0;

        while (!q.isEmpty()) {
            int[] a = q.pop(); // index, 우선순위
            
            if (a[1] < pq.peek()) {
                q.offer(a);
                continue;
            }
            
            // 우선순위랑 동일하거나 ~~
            pq.poll();
            temp[idx++] = a[0];
        }
        
        int answer = 0;
        
        for (int i=0; i<priorities.length; i++) {
            //System.out.println(temp[i]);
            if(temp[i] == location) {
                answer = i;
            }
        }
        
        return answer+1;
    }
}