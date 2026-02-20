const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const grid = input.slice(1).map(line => line.split(' ').map(Number));

// Please Write your code here.
const dx = [1, -1, 0, 0], dy = [0, 0, 1, -1];
let answer = 0;

for(let i=0; i<n; i++){
    for(let j=0; j<n; j++){
        let cnt = 0;
        let [x, y] = [i, j];

        for(let k=0; k<4; k++){
            let nx = x + dx[k];
            let ny = y + dy[k];

            if(0<=nx && nx<n && 0<=ny && ny<n && grid[nx][ny] ===  1){
                cnt += 1
            }
        }
        
        if(cnt >= 3) answer += 1;
    }
}

console.log(answer)