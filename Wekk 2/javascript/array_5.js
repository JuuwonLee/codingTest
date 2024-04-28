function solution(dirs){
    let answer = 0
    
    let ox = 5;
    let oy = 5;
    let nx = ox;
    let ny = oy;
    const ans = new Set();
    
    for(let i = 0;i<dirs.length;i++){
        nx, ny = newCordination(ox, oy, dirs[i])
        // console.log(nx+", "+ny);
        
        if (rightLine(nx, ny)){
            
            ans.add([ox, oy, nx, ny]);
            ans.add([nx, ny, ox, oy]);
            ox, oy = nx, ny   
        }
    }
        
    console.log(ans);
            
    answer = ans.length /2
      
    return answer
}

function rightLine(x, y){
    return 0 <= x < 11 && 0 <= y < 11
}
function newCordination(ox, oy, dir){
    let nx = ox
    let ny = oy
    if (dir == 'U')
        ny += 1 
    else if (dir == 'D')
        ny -= 1 
    else if (dir == 'R')
        nx += 1
    else if (dir == 'L')
        nx -= 1
    
    return nx, ny

}

solution("ULURRDLLU");