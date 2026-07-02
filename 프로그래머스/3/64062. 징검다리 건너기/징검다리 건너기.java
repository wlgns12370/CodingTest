class Solution {
    public boolean isOk(int[] stones, int cnt, int k) {
        int temp = 0;
        int flag = 0;
        for (int stone : stones) {
            temp = stone - (cnt-1);
            
            // 디딤돌 사용
            if (temp <= 0) {
                flag += 1;
                
                // 한정된 디딤돌보다 더 사용
                if (flag > k-1) {
                    return false;
                }
            } else {
                flag = 0;
            }
        }
        
        return true;
    }
    
    public int max_arr(int[] stones) {
        int temp = stones[0];
        for (int data : stones) {
            if (temp < data) {
                temp = data;
            }
        }
        return temp;
    }
    
    public int solution(int[] stones, int k) {
        
        int answer = 0;
        int lo = 0;
        int mid = 0;
        
        int hi = max_arr(stones)+1;
        
        while (lo <= hi) {
            mid = (lo+hi) / 2;
            if(isOk(stones, mid, k)) {
                answer = mid;
                lo = mid+1;               
            } else{
                hi = mid-1;
            }
        }
        return answer;
    }
}