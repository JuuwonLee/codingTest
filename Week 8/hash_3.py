from itertools import combinations, permutations

def solution(orders, course):
    answer = []
    dict = {}
    for order in orders :
        tmpArr = list(order) # "ABC" => ['A', 'B', 'C']

        for num in course :
            combi = list(combinations(tmpArr, num)) # num만큼의 수를 tmpArr에서 combination
            # print(combi, "//")
            if len(combi) > 0 :
                for arr in combi :
                    result = ''.join(s for s in arr)

                    # print(result)
            if result in dict :
                dict[result] += 1
            else : 
                dict[result] = 1
    print(dict)
        

    return answer
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))