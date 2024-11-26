/**
 * 알고리즘
 * - 각 자리의 더한 값과 뺀 값을 인자로 받아서 DFS를 한다.
 * - 모든 조합을 탐색하여 total이 target과 같은 경우의 수를 count한다.
 *
 * 시간복잡도
 * - O(2^n): 각 숫자에 대해 더하기와 빼기 두 가지 선택이 가능하므로,
 *           n개의 숫자에 대해 2^n개의 조합이 생성된다.
 * 자료구조
 * - int형 변수 answer: target에 해당하는 수의 개수를 저장하는 변수
 */
class Solution {
    private int answer = 0;
    private int n;
    private int[] numbers;
    private int target;

    void dfs(int v, int total) {
        if(v == n) {
            if(total == target) {
                answer += 1;
            }
            return;
        }
        else {
            dfs(v+1, total + numbers[v]);
            dfs(v+1, total + (-1 * numbers[v]));
        }
    }

    public int solution(int[] numbers, int target) {
        this.numbers = numbers;
        this.target = target;
        n = numbers.length;
        dfs(0, 0);
        return answer;
    }
}