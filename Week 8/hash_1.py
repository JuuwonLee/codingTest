def solution(genres, plays):
    answer = []
    dict = {}

    for i in range(len(genres)) :
        if genres[i] in dict :
            sum = dict[genres[i]][0] + plays[i]
            dict[genres[i]][0] = sum
            dict[genres[i]][1].append(i)
        else :
            dict[genres[i]] = [plays[i], [i]]
    
    
    sorted_dict = sorted(dict.items(), key= lambda item:item[1][0], reverse=True)
    # print(sorted_dict)
    

    for i in range(len(sorted_dict)) :
        # genre = sorted_dict[i][0]
        # print(genre)
        list = sorted_dict[i][1][1]

        if len(list) == 1 :
            answer.append(list[0])
        else :
            temp_dict = {}
            for j in range(len(list)) :
                temp_dict[list[j]] = plays[list[j]]
            
            sorted_temp_dict = sorted(temp_dict.items(), key = lambda item : item[1], reverse=True) 
            answer.append(sorted_temp_dict[0][0])
            answer.append(sorted_temp_dict[1][0])


            # print(sorted_temp_dict)



    

    

    
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))