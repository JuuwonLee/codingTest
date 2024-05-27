# 모든 유저는 [유저 아이디]로 구분한다.
# 첫 단어는 Enter, Leave, Change 중 하나이다.
# 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
# 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
def solution(record):
    answer = []
    dict = {}
    
    for s in record :
        tmp_list = s.split(' ')
        
        # print(tmp_list)
        if tmp_list[0] == 'Enter' or tmp_list[0] == 'Change' :
            # if id not in dict :
            userId = tmp_list[1]
            nickName = tmp_list[2]
            dict[userId] = nickName
        else : # 'Leave' 일때
            continue       

    for s in record :
        tmp_list = s.split(' ')
        userId = tmp_list[1]
        nickName = dict[userId]
        if tmp_list[0] == 'Enter' :
            tmp_str = nickName + "님이 들어왔습니다."
            answer.append(tmp_str)
        elif tmp_list[0] == 'Leave' :
            tmp_str = nickName + "님이 나갔습니다."
            answer.append(tmp_str)
            
    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))