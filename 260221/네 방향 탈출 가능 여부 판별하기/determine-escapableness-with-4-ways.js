const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const grid = input.slice(1, n + 1).map(line => line.split(' ').map(Number));

// Please Write your code here.
const dx = [1, -1, 0, 0]
const dy = [0, 0, 1, -1]

const visited = Array.from({ length: n }, () => Array(m).fill(false));

const queue = [];
queue.push([0, 0]);
visited[0][0] = true

function isRange(x, y) {
    return 0 <= x && x < n && 0 <= y && y < m
}

while (queue.length > 0) {
    let [x, y] = queue.pop();

    for (let i = 0; i < 4; i++) {
        nx = x + dx[i]
        ny = y + dy[i]

        if (isRange(nx, ny) && !visited[nx][ny] && grid[nx][ny] == 1) {
            queue.push([nx, ny])
            visited[nx][ny] = true
        }
    }

}

if (visited[n - 1][m - 1]) {
    console.log(1)
} else {
    console.log(0)
}