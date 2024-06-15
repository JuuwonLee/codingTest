def solution(command):
    curX = 0
    curY = 0
    directionArr = ["y+", "x+", "y-", "x-"] 
    curDirectionIdx = 0

    answer = []

    for direction in command :
        
        if direction == "R": 
            curDirectionIdx = (curDirectionIdx + 1) % len(directionArr)
        elif direction == "L": 
            curDirectionIdx = (curDirectionIdx - 1) % len(directionArr)
        elif direction == "G": 
            if curDirectionIdx == 0 :
                curY = curY + 1
            elif curDirectionIdx == 1 :
                curX = curX + 1
            elif curDirectionIdx == 2 :
                curY = curY - 1
            else :
                curX = curX - 1
        else :
            if curDirectionIdx == 0 :
                curY = curY - 1
            elif curDirectionIdx == 1 :
                curX = curX - 1
            elif curDirectionIdx == 2 :
                curY = curY + 1
            else :
                curX = curX + 1

    answer.append(curX)
    answer.append(curY)
    return answer

command = "GRGLGRG"

print(solution(command))