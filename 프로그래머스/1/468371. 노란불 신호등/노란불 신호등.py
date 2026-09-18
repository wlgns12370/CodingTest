def solution(signals):
    n = len(signals)
    k = 2000000
    
    arr = [[""]*k for i in range(n)]
    
    for sig_len, signal in enumerate(signals):
        idx=0
        s_idx = 0
        temp = signal[0]
        while(idx<k):
            
            if s_idx%3 == 0:
                arr[sig_len][idx] = "G"
            elif s_idx%3 == 1:
                arr[sig_len][idx] = "Y"
            elif s_idx%3 == 2:
                arr[sig_len][idx] = "R"
            
            temp -= 1
            if temp == 0:
                s_idx+=1
                temp = signal[s_idx%3]
            idx+=1
    
    answer = -1
    for i in range(k):
        flag = 1
        for j in range(n):
            if arr[j][i] != "Y":
                flag = 0
                break
        if flag == 1:
            return i+1
    
    return answer