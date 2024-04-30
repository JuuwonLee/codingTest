def solution(s):
    answer = 0 # default 값은 실패
    
    length = len(s)

    stack = []
    
    
    for i in range(length) :
        if i == 0 : #  인덱스가 0이면 무조건 push
            stack.append(s[i]) 
        else : # 인덱스가 0이 아니면
            if len(stack) > 0 and stack[-1] == s[i] : # stack 안에 element가 있고, stack의 제일 위에 있는 값과 s[i]가 같으면 pop
                stack.pop()
            else : # stack 안에 element가 없거나, stack의 제일 위에 있는 값과 s[i]가 다르면 push
                stack.append(s[i])
            
    if len(stack) == 0 :
        answer = 1
    
    return answer