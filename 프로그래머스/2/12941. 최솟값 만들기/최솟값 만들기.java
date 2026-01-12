import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        
        PriorityQueue<Integer> minPq = new PriorityQueue<>();
        PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
            
        for (int num : A) {
            minPq.add(num);
        }
        
        for (int num : B) {
            maxPq.add(num);
        }
        
        int result = 0;
        while(!minPq.isEmpty()) {
            result += (minPq.poll()*maxPq.poll());
        }

        return result;
    }
}