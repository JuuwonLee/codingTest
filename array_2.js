function solution(answers) {
    var ans = [];
    
    ans = cntAns(answers);
    
    const maxValue = Math.max(...ans);
    var fianlAns = [];
    ans.forEach((num, idx) => {
       if(maxValue == num)fianlAns.push(idx+1);
    });    
    
    return fianlAns;
}

function cntAns(answers) {
    const ansSet = 
        [[1, 2, 3, 4, 5, 0, 0, 0, 0, 0],
         [2, 1, 2, 3, 2, 4, 2, 5, 0, 0],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]];
    let cnt = [0, 0, 0];
    
    answers.forEach((num, idx) => {
        if(num == ansSet[0][idx % 5 ])cnt[0]++;
        if(num == ansSet[1][idx % 8 ])cnt[1]++;
        if(num == ansSet[2][idx % 10 ])cnt[2]++;
        
    });

    return cnt;
}