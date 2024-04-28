function solution(arr1, arr2) {
    var answer = [[]];
   
   const rows = arr1.length;
   const columns = arr2[0].length;
   
   answer = Array.from(new Array(rows), () => new Array(columns).fill(0));

   
   for(let i = 0; i < rows; i++){
       for(let j = 0; j < columns; j++){
           for(let k = 0; k < arr1[0].length; k++){
               answer[i][j] += arr1[i][k] * arr2[k][j];
           }
       }
   }
   return answer;
}