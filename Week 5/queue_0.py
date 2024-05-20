def solution(n, k):
    answer = 0
    que = []
    for i in range(n) :
        que.append(i+1) # que : [1, 2, 3, ..., n-1, n]
    
    cur = 1
    while len(que) > 1 :
        print(cur, que)
        for i in range(cur, cur + k - 1 , 1) : # cur ~ cur + k - 1
            tmp = que.pop(0)
            que.append(tmp)
        
        que.pop(0) # k번째 삭제
        cur = que[0]
        
    answer = que[0]
    return answer
print(solution(5,2))