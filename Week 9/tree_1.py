def solution(n,a,b):
    answer = 0

    round = 1

    players = []
    winner = []

    for i in range(n) : # 1라운드에서 players에 선수들 번호 넣기
        winner.append(i+1)

    while(round <=  n-1 ) : # n은 무조건 짝수라 총 경기 횟수는 n-1

        if answer >= 1 :
            break
        
        print(players)
        
        if len(players) > 0 :
            winner.clear()
            for i in range(len(players)) :
                winner.append(players[i])
            players.clear()

        # 각 round에서 a,b가 만났는지 먼저 확인
        if a in winner and b in winner :
            a_idx = winner.index(a) + 1 # a 인덱스 
            b_idx = winner.index(b) + 1 # b 인덱스


            if a_idx % 2 == 1 and a_idx + 1 == b_idx: # a 인덱스가 홀수, a 다음 b
                answer = round
                break
            elif a_idx % 2 == 0 and a_idx - 1 == b_idx : # a 인덱스가 짝수, b 다음 a
                answer = round
                break
        
        
        for i in range(1, len(winner)+1, 1) :
            if a_idx % 2 == 0 and a_idx - 1 == i: # a 인덱스가 짝수, i = a_idx - 1
                players.append(a)
                continue
            elif a_idx % 2 == 1 and a_idx + 1 == i: # a 인덱스가 홀수, i = a_idx + 1
                players.append(a)
                continue

            if b_idx % 2 == 0 and b_idx - 1 == i: # b 인덱스가 짝수, i = b_idx - 1
                players.append(b)
                continue
            elif b_idx % 2 == 1 and b_idx + 1 == i: # b 인덱스가 홀수, i = b_idx + 1
                players.append(b)
                continue

            if winner[i-1] != a and winner[i-1] != b and (i) % 2 == 1 :# 두 선수 중 무조건 첫번째 선수가 이긴걸로 간주 (a,b 제외)
                players.append(winner[i-1])


        round += 1

    return answer

N = 8
A = 4
B = 7
# answer = 3

print(solution(N,A,B))