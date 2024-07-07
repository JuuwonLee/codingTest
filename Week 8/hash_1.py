def solution(genres, plays):
    answer = []
    dict = {}

    for i in range(len(genres)) :
        if genres[i] in dict : # 만약 장르가 딕셔너리의 키로 이미 있다면
            sum = dict[genres[i]][0] + plays[i] # 기존 장르 합에 더하기
            dict[genres[i]][0] = sum # value의 0번째 인수는 sum, 
            dict[genres[i]][1].append(i) # value의 1번째 인수는 그 장르에 속하는 노래의 고유번호
        else :
            dict[genres[i]] = [plays[i], [i]] # 만약 장르가 딕셔너리의 키로 없다면, 초기화
    
    
    sorted_dict = sorted(dict.items(), key= lambda item:item[1][0], reverse=True) # sum이 높은 순대로 정렬(내림차순)
    # print(sorted_dict) [('pop', [3100, [1, 4]]), ('classic', [1450, [0, 2, 3]])]
    

    for i in range(len(sorted_dict)) : # 각각의 장르마다
        # genre = sorted_dict[i][0]
        # print(genre)
        list = sorted_dict[i][1][1] # list는 그 장르에 속하는 노래의 고유번호들

        if len(list) == 1 : # 갯수가 1개면
            answer.append(list[0])
        else : # 갯수가 1개보다 많으면(0은 절대 안되니까 제외)
            temp_dict = {}
            for j in range(len(list)) :
                temp_dict[list[j]] = plays[list[j]] # 키는 노래의 고유 번호, value는 그 노래가 재생된 횟수
            
            sorted_temp_dict = sorted(temp_dict.items(), key = lambda item : item[1], reverse=True) # value를 기준으로 내림차순 정렬
            answer.append(sorted_temp_dict[0][0]) # 가장 순위가 높은 두개를 answer에 추가
            answer.append(sorted_temp_dict[1][0])


            print(sorted_temp_dict)
    
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))