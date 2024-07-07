# from itertools import combinations, permutations

# def solution(orders, course):
#     answer = []
#     dict = {}
#     for i in range(len(orders)) :
#         tmpArr = list(orders[i]) # "ABC" => ['A', 'B', 'C']

#         for num in course :
#             combi = list(combinations(tmpArr, num)) # num만큼의 수를 tmpArr에서 combination
#             print(combi, "//")
            
#             for arr in combi :
#                 result = ''.join(s for s in arr) #['a', 'b'] => "ab"

#                 if result not in dict :
#                     dict[result]=[i] # 초기화
#                 else :
#                     if i not in dict[result] :
#                         dict[result].append(i)
#     print(dict)
#     # 두명이상인지 확인 필요

#     return answer


from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()

        if len(most_ordered) == 0:
            continue

        max_value = most_ordered[0][1]
        print(max_value)
        
        for key, value in most_ordered:
            
            if value > 1 and value == max_value:
                answer.append(''.join(key))

    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))

