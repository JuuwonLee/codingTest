from collections import deque

def solution (menu, order, k):
    answer = 0
    n = len (order)
    queue = deque()
    i = 0
    time = 0

    while queue or i < n:
        if not queue:
            time = (i * k) + menu[order[i]]
            i += 1 
        else:
            x = queue.popleft()
            time += menu[x]
        while i < n and i <= ((time - 1) // k):
            queue.append(order[i])
            i += 1
        answer = max(answer,len(queue))
    
    return answer + 1