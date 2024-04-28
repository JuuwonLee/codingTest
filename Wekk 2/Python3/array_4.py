def solution(N, stages):
    answer = [0] * N
    noclear = [0] * (N+1) # 각 단계 별 도전중인 사용자
    fails = [0] * N  
    total = len(stages)
    
    for stage in stages : # 각 단계의 도전자수
        noclear[stage-1] += 1
        
    
    for i in range(0, N) :
        if noclear[i] == 0 :
            fails[i] =0
        else :
            fails[i] = noclear[i] / total
            total -= noclear[i]
        

    dic = {}
    for i in range(0, N) :
        dic[i+1] = fails[i]
    
    # print(dic)
    
    
    answer = sorted(dic, key=lambda x:dic[x], reverse=True)
    

    return answer