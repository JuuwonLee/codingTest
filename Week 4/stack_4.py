def solution(board, moves):
    answer = 0
    length = len(board[0])
    
    stack = []
    
    for i in range(len(moves)) :
        col = moves[i] - 1 # moves 원소값
        row = findTopRow(length, board, col) -1
        
        print(row, col)
        
        temp_value = board[row][col]
        # print(temp_value)
        
        if temp_value != 0 :
            stack.append(temp_value)
    
        board[row][col] = 0
        # print(stack)
        if len(stack) >= 2 :
            if stack[-2] == stack[-1] :
                stack.pop()
                stack.pop()
                answer += 2
            # print(stack[-2], stack[-1])
    return answer

def findTopRow(length, board, col) :
    result = 0
    
    for i in range(length) :
        if board[i][col]  != 0 :
            result = i+1
            break
    
    return result
