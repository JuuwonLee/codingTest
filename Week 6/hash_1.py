def solution(participant, completion):
    answer = ''
    length = len(participant)
    
    participant.sort()
    completion.sort()
    
    print(participant)
    print(completion)
    answer = participant[length-1]
    for i in range(length-1) :
        if participant[i] == completion[i] :
            continue
        else :
            if (i+1 <= length - 1) and participant[i+1] == completion[i]  :
                answer = participant[i]
                break

    
    return answer