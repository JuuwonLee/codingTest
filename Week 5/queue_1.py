
def solution(progresses, speeds):
    answer = []
    
    queue = progresses
    
    
    while len(queue) > 0 :
        # print(queue)
        for i in range(len(queue)) :
            queue[i] += speeds[i]
        
        if queue[0] < 100 :
            continue
        else :
            if len(queue) > 0 :
                queue.pop(0)
                speeds.pop(0)
                num = 1
                
                while len(queue) > 0 and queue[0] >= 100 :
                    queue.pop(0)
                    speeds.pop(0)
                    num += 1        
                
                answer.append(num)
                
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))