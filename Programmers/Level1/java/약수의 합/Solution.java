/**
 * 알고리즘
 * - 자연수 i가 n의 제곱근까지 순회하며, 만약 i가 n의 약수이면 약수를 answer 변수에 더한다.
 * - 이때 약수 i와 n/i가 같다면, 하나의 약수만 더하고, 그렇지 않으면 두 개의 약수를 더한다.
 * 
 * 시간복잡도
 * - O(√n): n의 제곱근까지 순회하므로.
 * 
 * 자료구조
 * - int형 변수 answer: 약수를 저장하는 변수.
 * - int형 변수 i: 순회를 위한 변수.
 */
public class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 1;
			while(true) {
				if(n/i < i) {
					break;
				}
				if(n%i == 0) {
					if(n/i == i) {
						answer += i;
					}
					else {
						answer += i;
						answer += n / i;
					}
				}
				i++;
			}
        return answer;
    }
}