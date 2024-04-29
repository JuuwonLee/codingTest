function solution(N, stages){
    
    
    // answer = [];
    noclear = Array.from(new Array(N+1).fill(0));// 각 단계 별 도전중인 사용자
    // noclear = [];
    fails = Array.from(new Array(N).fill(0));// 각 단계 별 실패율
    //  fails = [];
    total = stages.length;
    
    stages.forEach(stage => {  // 각 단계의 도전자수
        noclear[stage-1] += 1;
    });  
        
    for(let i = 0;i < N; i++){
        if(noclear[i] == 0){
            fails[i] = 0
        } else {
            fails[i] = noclear[i] / total
            total -= noclear[i]
        }
    }
        
    
    // console.log(fails)

    answer = Array.from(new Array(N).fill(0));
    const hash = new Map();

    for(let i = 0;i < N; i++){
        hash.set(i+1, fails[i]);
    }

    
    // console.log(map)
    
    
    answer = [...hash.entries()]
        .sort((a, b) => b[1] - a[1])
        .map((num) => num[0]);
    

    return answer
}

stages	= [2, 1, 2, 6, 2, 4, 3, 3];

// console.log(solution(5, stages));