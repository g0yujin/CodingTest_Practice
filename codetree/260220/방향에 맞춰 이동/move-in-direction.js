const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);

const dx=[1, -1, 0, 0];
const dy =[0, 0, -1, 1];
let [x, y] = [0, 0];

for(let i=1; i<=n; i++){
    let [dir, num] = input[i].split(" ");
    num = Number(num)

    if(dir == 'E'){
        x += dx[0] * num;
    }
    else if(dir == 'W'){
        x += dx[1] * num
    }
    else if(dir == 'S'){
        y += dy[2] * num;
    }
    else{
        y += dy[3] * num;
    }
   

}
console.log(x, y)