def solution(id_list, report, k):
    answer = []
    dict1 = {}
    dict2 = {}
    
    for id in id_list : # 초기화
        dict1[id] = []
        dict2[id] = 0

    for rp in report :
        list = rp.split(" ")
        reporter = list[0] # 신고자
        badUser = list[1] # 신고당한 유저
        
        if badUser not in dict1[reporter] :
            dict1[reporter].append(badUser) # 신고자가 신고한 유저 리스트에 badUser를 추가
            dict2[badUser] += 1 # badUser는 본인이 신고당한 횟수에 1을 더함
        
    print(dict1, dict2)
    
    for id in id_list :
        list = dict1[id]
        # print(list)
        if len(list) == 0 : # 해당 id가 신고한 유저가 없으면
            answer.append(0)
        else :
            num = 0 # 초기화
            for badUser in list :
                if dict2[badUser] >= k : # 해당 id가 신고한 badUser가 신고당한 횟수가 k보다 많으면        
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