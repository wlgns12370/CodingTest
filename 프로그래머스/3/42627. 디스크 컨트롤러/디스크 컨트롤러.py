import heapq

def solution(jobs):
    jobs.sort() 
    
    l = len(jobs)
    q = []
    
    time = 0
    total_tat = 0
    job_idx = 0
    processed = 0
    
    while processed < l:
        while job_idx < l and jobs[job_idx][0] <= time:
            rt, et = jobs[job_idx]
            heapq.heappush(q, (et, rt))
            job_idx += 1
            
        if q:
            et, rt = heapq.heappop(q)
            time += et
            total_tat += (time - rt)
            processed += 1
            
        else:
            time = jobs[job_idx][0]
            
    answer = total_tat // l
    return answer