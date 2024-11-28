"""
  1. 아이디어
    - progresses와 speeds의 합이 100을 넘을 때, 각각의 큐 가장 앞의 값을 pop 한다.
    - 만약 더 이상 pop할 상태가 아니라면(작업이 완료되어서 배포됐다면), answer에 배포한 progresse의 수를 추가한다

  2. 시간 복잡도
  - O(N) : N은 progresses + time*speeds의 값이 가장 큰 경우

  3. 자료구조
  - int형 변수 time: 작업의 시간
"""

def solution(progresses, speeds):
    answer = []
    time = 1
    cnt = 0
    while True:
        if progresses == []:
            answer.append(cnt)
            break

        if (progresses[0] + time*speeds[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1
    return answer