def solution(id_list, report, k):
    answer = []
    dict1 = {}
    dict2 = {}
    
    for id in id_list : # 초기화
        dict1[id] = []
        dict2[id] = 0

    for rp in report :
        list = rp.split()
        reporter = list[0]
        badUser = list[1]
        
        if badUser not in dict1[reporter] : 
            dict1[reporter].append(badUser)
            dict2[badUser] += 1
        
    # print(dict1, dict2)
    
    for id in id_list :
        list = dict1[id]
        # print(list)
        if len(list) == 0 :
            answer.append(0)
        else :
            num = 0
            for badUser in list :
                if dict2[badUser] >= k :        
                    num += 1
            answer.append(num)
    
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

print(solution(id_list, report, k))