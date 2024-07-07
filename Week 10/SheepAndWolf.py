from collections import deque

# [1, 8], [2, 4], [], [], [3, 6], [], [5], [], [7, 9], [10, 11], [], []]
    

def solution(info, edges):
    answer = 0 #최대 양의 수를 저장할 수 초기화


    # 트리 구축
    dict = [[] for _ in range(len(info))]

    for edge in edges:
        dict[edge[0]].append(edge[1])
    print(dict)
    
    q = deque([(0, 1, 0, set())]) # BFS를 위한 큐 생성 및 초기 상태 설정 (현재 위치, 양의 수, 늑대의 수, 방문한 노드 집합)

    # BFS 시작
    while q:
    # 큐에서 상태 가져오기
        current, sheep_count, wolf_count, visited = q.popleft()
        # 최대 양의 수 업데이트
        answer = max(answer, sheep_count)
        # 방문한 노드 집합에 현재 노드의 이웃 노드 추가
        visited.update(dict[current])
        # 인접한 노드들에 대해 탐색
        for next_node in visited:
            if info[next_node]: # 늑대일 경우
                if sheep_count != wolf_count + 1:
                    q.append((next_node, sheep_count, wolf_count + 1, visited - {next_node}))
            else: # 양일 경우
                q.append((next_node, sheep_count + 1, wolf_count, visited - {next_node}))

            
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))