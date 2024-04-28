def solution(dirs):
    answer = 0
    
    ox = 5
    oy = 5
    
    ans = set()
    
    for dir in dirs :
        # print(dir)
        nx, ny = newCordination(ox, oy, dir)
        if not rightLine(nx, ny) :
            continue;
        ans.add((ox, oy, nx, ny))
        ans.add((nx, ny, ox, oy))
        ox, oy = nx, ny
            
    answer = len(ans) /2
      
    return answer


def rightLine(x, y):
    return 0 <= x < 11 and 0 <= y < 11
    
def newCordination(ox, oy, dir) :
    nx = ox
    ny = oy
    if dir == 'U' :
        ny += 1 
    elif dir == 'D' :
        ny -= 1 
    elif dir == 'R' :
        nx += 1
    elif dir == 'L' :
        nx -= 1
    
    return nx, ny