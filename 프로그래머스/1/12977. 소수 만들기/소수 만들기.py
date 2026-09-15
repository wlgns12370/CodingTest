import math
def solution(nums):
    
    def isOk(number):
        for q in range(2,int(math.sqrt(number))+1):
            if number % q == 0:
                return False
        return True
    
    l = len(nums)
    visited = [False for _ in range(l)]
    result = set()
    def dfs(num,lis):
        if num < 3:
            for next in range(0,l):
                if visited[next] == False:
                    visited[next] = True
                    dfs(num+1,lis+[nums[next]])
                    visited[next] = False
        else:
            result.add(tuple(sorted(lis)))
                
                
    dfs(0,[])
    
    answer = 0
    for a,b,c in result:
        if isOk(a+b+c):
            answer += 1

    return answer