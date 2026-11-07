import java.util.*;
class Solution {
    static int n;
    static boolean[] visited;
    static Ticket[] sortedTickets;
    static Deque<String> path;
    
    public class Ticket implements Comparable<Ticket> {
        String cur;
        String target;
        
        public Ticket(String cur, String target) {
            this.cur = cur;
            this.target = target;
        }
        
        @Override
        public int compareTo(Ticket o) {
            int res =  this.cur.compareTo(o.cur);
            if (res != 0) {
                return res;
            }
            int res2 = this.target.compareTo(o.target);
            if (res2 != 0) {
                return res2;
            }
            return 0;
        }
    }
    
    public static boolean dfs(String current, int len) {
        if (len == n) {
            // 끝나는 조건
            return true;
        }
        
        for (int i = 0; i < n; i++) {
            
            if (visited[i]) {
                continue;
            }
            
            // 선택할 수 없는 티켓
            if (!sortedTickets[i].cur.equals(current)) {
                continue;
            }
            
            visited[i] = true;
            path.offer(sortedTickets[i].target);
            
            // true로 끝나는 경우 방문 취소와 경로 없애기 수행 x
            if(dfs(sortedTickets[i].target, len+1)){
                return true;
            }
            
            visited[i] = false;
            path.pollLast();
        }
        return false;
    }
    
    
    public String[] solution(String[][] tickets) {
        
        n = tickets.length;
        visited = new boolean[n];
        path = new ArrayDeque<>();
        sortedTickets = new Ticket[n];
        
        for (int i =0; i < n; i++) {
            sortedTickets[i] = new Ticket(tickets[i][0],tickets[i][1]);
        }
        
        Arrays.sort(sortedTickets);
        
        path.offer("ICN");
        
        dfs("ICN",0);
        
        String[] answer = new String[n + 1];

        for (int i = 0; i < n + 1; i++) {
            answer[i] = path.pop();
        }

        return answer;
    }
}