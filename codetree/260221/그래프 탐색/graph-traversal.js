const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const edges = [];
for (let i = 1; i <= m; i++) {
    edges.push(input[i].split(' ').map(Number));
}
// Please Write your code here.
let graph = Array.from({ length: n + 1 }, () => []);

for (let i = 0; i < m; i++) {
    a = edges[i][0]
    b = edges[i][1]

    graph[a].push(b);
    graph[b].push(a);
}

const visited = Array(n + 1).fill(false);
let answer = 0;

function dfs(v) {
    visited[v] = true // 방문처리

    for (let next of graph[v]) {
        if (!visited[next]) {
            answer += 1
            dfs(next)
        }
    }

}
dfs(1)
console.log(answer)