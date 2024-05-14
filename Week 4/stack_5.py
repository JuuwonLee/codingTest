
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
                k = dic[k][0] # x번동안 타고 올라가기
        elif cmd[i][0] == "D" :
            tmp_list = cmd[i].split(' ')
            x = int(tmp_list[1])
            for _ in range(x) : # x번동안 타고 내려가기
                k = dic[k][1]
        elif cmd[i] == "C" :
            stack.append(k) # 삭제할 인덱스 넣기
            dic[k][2] = 'X' # 삭제할 인덱스 딕셔너리 마지막 원소에 X 표시하기
            prev = dic[k][0] # k 인덱스의 이전 인덱스
            post = dic[k][1] # k 인덱스의 다음 인덱스
            
            if prev == None: # k가 첫 행일때
                k = dic[k][1] # k는 k의 다음 인덱스가 됨
                dic[post][0] = None # k의 다음인덱스의 딕셔너리의 첫번째 값에 None 값 넣기
            elif post == None: # k가 마지막 행일때
                k = dic[k][0] # k는 k의 이전 인덱스가 됨
                dic[prev][1] = None # k의 이전 인덱스의 딕셔너리의 두번째 값에 None 값 넣기
            else:
                k = dic[k][1] # k는 k의 다음 인덱스가 됨
                dic[prev][1] = post
                dic[post][0] = prev

            
        else :
            pop_idx = stack.pop()
            prev = dic[pop_idx][0]
            post = dic[pop_idx][1]

            dic[pop_idx][2] = 'O' # 복구할 인덱스에 해당하는 딕셔너리의 마지막 원소에 O 표시하기

            if post == None : # 복구할 행이 마지막일 때
                dic[prev][1] = pop_idx
            elif prev == None : # 복구할 행이 처음일 때
                dic[post][0] = pop_idx
            else :
                dic[prev][1] = pop_idx
                dic[post][0] = pop_idx
        # print('dic : ',dic)
        # print('stack : ',stack)

    for i in range(n) :
        answer += dic[i][2]
    return answer