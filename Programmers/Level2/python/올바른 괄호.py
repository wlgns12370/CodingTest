"""
    1. 아이디어
    - 여는 괄호일 경우 stack에 저장한다.
    - 닫는 괄호일 경우 stack에서 pop 한다. 이때 stack이 비어있다면, 닫는 괄호가 더 많은 경우이므로 False
    - 모든 s를 탐색하고 stack이 비어있지 않다면, 여는 괄호가 더 많은 경우이므로 False
    
    2. 시간 복잡도
    - O(S) S : 문자열 s의 길이(100,000 이하의 자연수)
    
    3. 자료구조
    - stack 배열
"""
def solution(s):
    answer = True
    stack = []

    for data in s:
        if data == '(':
            stack.append('(')
        elif data == ')':
            # 닫는 괄호가 더 많은 경우
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
    # 여는 괄호가 더 많은 경우
    if len(stack) != 0:
        answer = False

    return answer

#Test Code
print(solution("()()"))