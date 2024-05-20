def solution(cards1, cards2, goal):
    answer = "No"
    result = []
    
    for word in goal : 
        if len(cards1) > 0 and cards1[0] == word : # cards1의 첫번째 인덱스의 단어와 같을때
            cards1.pop(0) # cards1의 첫번째 인덱스 pop
            result.append(word) # result에 해당 word push
            continue # 다음 word로 넘어가기
        elif len(cards2) > 0 and cards2[0] == word : # cards2의 첫번째 인덱스의 단어와 같을때
            cards2.pop(0) # cards2의 첫번째 인덱스 pop
            result.append(word) # result에 해당 word push
            continue # 다음 word로 넘어가기
        else :
            break # 둘 중에 같은게 안나오면 break
        
    if result == goal :
        answer = "Yes"

    
    return answer


cards1 = ["i", "drink", "water"]	
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]



print(solution(cards1, cards2, goal))