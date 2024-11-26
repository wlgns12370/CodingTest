/**
 * 알고리즘
 * - 나머지 연산을 통해 끝자리를 추출하여 answer에 더한다.
 * - 10으로 나누어 몫을 구한다. 이때 몫이 0이 될 때까지 반복한다.
 *
 * 시간복잡도
 * - O(logN) 자릿수 순회
 *
 * 자료구조
 * - int형 변수 answer: 자릿수의 합을 저장하는 변수
 */
class Solution {
    public int solution(int n) {
        int answer = 0;
        while(true) {
            if(n / 10 == 0) {
                answer += n;
                break;
            }
            answer += n%10;
            n /= 10;
        }
        return answer;
    }
}