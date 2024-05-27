# 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개
# 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)) :
        dict = constructDict(want, number)
        
        for j in range(i, i + 10, 1) : # i ~ i + 9
            if j <= len(discount) - 1 :
                if discount[j] in dict :
                    # print("exist",discount[j], dict[discount[j]])
                    dict[discount[j]] = dict[discount[j]] - 1
                # else :
                    # print("none",discount[j])
                    
        
        # print("next goods")
        # print(dict)

        allZero = True
        for j in range(len(want)) :
            if dict[want[j]] > 0 :
                allZero = False
                break
                

        if allZero == True :
            answer += 1
                
    return answer
                 
def constructDict(want, number) :
    dict = {}
    for i in range(len(want)) :
        dict[want[i]] = number[i]
                 
    return dict

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))