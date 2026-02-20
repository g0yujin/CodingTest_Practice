const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const grid = input.slice(1, n + 1).map(row => row.split(' ').map(Number));

// Please Write your code here.
dx = [0, 1]
dy = [1, 0]

const visited = Array.from({ length: n }, () =>
    Array(m).fill(false)
)

function isRange(x, y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

function dfs(x, y) {
    visited[x][y] = true

    for (let i = 0; i < 2; i++) {
        nx = x + dx[i]
        ny = y + dy[i]
        if (isRange(nx,ny) && !visited[nx][ny] && grid[nx][ny] == 1){
            dfs(nx, ny)
        }
    }

}

dfs(0,0)

if(visited[n-1][m-1]){
    console.log(1)
}else{
    console.log(0)
}

