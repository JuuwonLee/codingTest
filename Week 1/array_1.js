function solution(numbers) {
    var answer = []
    
    for(let i = 0;i<numbers.length;i++){
        for(let j = 0;j<numbers.length;j++){
            if(i != j){
                var element = numbers[i]+numbers[j]
                if (!answer.includes(element))
                        answer.push(element)
            }
        }
    }
    
    answer.sort(function(a, b)  {
        return a - b;
    })
    
    return answer;
}