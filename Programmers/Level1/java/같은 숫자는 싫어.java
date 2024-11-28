/**
 * 알고리즘
 * - 다른 숫자가 나올때까지 탐색한다.
 * - 만약 다른 숫자가 나온다면 해당 숫자를 새로운 List에 추가한다.
 *
 * 시간복잡도
 * - O(N)
 *
 * 자료구조
 * - int[] answer : 같은 숫자를 삭제한 배열
 */

import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> temp = new ArrayList<>();
        int point = -1;

        for(int i = 0; i < arr.length; i++) {
            if (arr[i] != point) {
                point = arr[i];
                temp.add(point);
            }
        }

        int[] answer = new int[temp.size()];
        for(int i = 0; i < temp.size(); i++) {
            answer[i] = temp.get(i);
        }
        return answer;
    }
}