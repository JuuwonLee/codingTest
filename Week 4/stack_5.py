
def solution(n, k, cmd):
    answer = ''
    
    stack = []
    
    arr = [0] * n
    dic = {}
    dic[0] = [None, 1, 'O']
    for i in range(1, n-1) :
        dic[i] = [i-1, i+1, 'O']
    
    dic[n-1] = [n-2, None, 'O']

    
    
    
    for i in range(len(cmd)) : # cmd 원소에 하나씩 접근
        # print('명령어 : ', cmd[i])
        # print('k 값 : ', k)
        if cmd[i][0] == "U" :
            tmp_list = cmd[i].split(' ')
            x = int(tmp_list[1])
            for _ in range(x):
                k = dic[k][0]
        elif cmd[i][0] == "D" :
            tmp_list = cmd[i].split(' ')
            x = int(tmp_list[1])
            for _ in range(x):
                k = dic[k][1]
        elif cmd[i] == "C" :
            stack.append(k) # 삭제할 인덱스 넣기
            dic[k][2] = 'X' # 삭제할 인덱스 딕셔너리 마지막 원소에 X 표시하기
            prev = dic[k][0]
            post = dic[k][1]
            
            if post == None:
                k = dic[k][0]
            else:
                k = dic[k][1]
            if prev == None:
                dic[post][0] = None
            elif post == None:
                dic[prev][1] = None
            else:
                dic[prev][1] = post
                dic[post][0] = prev

            
        else :
            pop_idx = stack.pop()
            prev_idx = dic[pop_idx][0]
            next_idx = dic[pop_idx][1]

            dic[pop_idx][2] = 'O' # 복구할 인덱스에 해당하는 딕셔너리의 마지막 원소에 O 표시하기

            if next_idx == None : # 복구할 행이 마지막일 때
                dic[prev_idx][1] = pop_idx
            elif prev_idx == None : # 복구할 행이 처음일 때
                dic[next_idx][0] = pop_idx
            else :
                dic[prev_idx][1] = pop_idx
                dic[next_idx][0] = pop_idx
        # print('dic : ',dic)
        # print('stack : ',stack)

    for i in range(n) :
        answer += dic[i][2]
    return answer

# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(8,2,cmd))