class Stack {
    constructor() {
      this._arr = [];
    }
    push(item) {
      this._arr.push(item);
    }
    pop() {
      return this._arr.pop();
    }
    peek() {
      return this._arr[this._arr.length - 1];
    }
      
    getSize() {
      return this._arr.length;
    }
  
    isEmpty() {
      return this.getSize() === 0;
    }
  
  }
  
  function solution(s){
      var answer = true;
      const len = s.length;
      
      if(s[0] == ')') {
          answer = false;
      } else {
          const stack = new Stack();
          for (const c of s) {
              if(c == '('){
                  stack.push(c);        
              } else {
                  stack.pop();  
              }
          }
          if(!stack.isEmpty()){
              answer = false;
          }
          // console.log(stack.getSize());
      }
       
      return answer;
  }