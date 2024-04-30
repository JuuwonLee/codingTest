from collections import deque

def solution(s):
    answer = 0
    
    length = len(s)
    
    for i in range(length) :
        
        deque_s = deque(s) # deque를 이용해서 rotate
        deque_s.rotate(-i)
        temp = list(deque_s) # deque를 list로 변환 (rightBracket의 파라미터로 넣기 위해서)
        
        if rightBracket(temp) == True :
            answer += 1
    return answer


    
    
def rightBracket(s):
    stack = [] # list로 stack 기능을 비슷하게 수행 가능
    cal_num = 0
    for c in s :
        # print(c)
        
        if c == '('  or c == '[' or c == '{' : 
            stack.append(c) # 여는 괄호는 push
            cal_num += 1  # 계산 횟수 1개 더하기
        else :
            if len(stack) == 0 : # stack에 아무것도 없으면 넘어가기
                continue
            else : 
                if c == ')' and stack[-1] == '(' : # 현재 인덱스에 해당하는 배열원소가 ) 이고 stack 제일 위에 있는 원소가 ( 이면 pop
                    stack.pop()
                elif c == ']' and stack[-1] == '[' :
                    stack.pop()
                elif c == '}' and stack[-1] == '{' :
                    stack.pop()
        # print(stack)    
    if len(stack) == 0 and cal_num > 0: # stack에 아무것도 남은게 없고 계산횟수가 1 이상이면 true
        return True
    else : # 그 외는 false
        return False
            