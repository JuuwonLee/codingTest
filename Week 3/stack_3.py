def solution(prices):
    length = len(prices)
    answer = [0] * length

    for i in range(length) :
        for j in range(i+1, length) :
            if prices[i] > prices[j] : # i초의 주식가격이 다음 초에서 떨어지면 
                answer[i] += 1
                break # 비교는 여기서 끝
            else : # i초의 주식가격이 다음 초에서 안떨어지면
                answer[i] += 1
  
    return answer
