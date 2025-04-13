import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, K, total;
	static char[][] map;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		T = Integer.parseInt(br.readLine());

		// 테스트케이스만큼 반복
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken()); // 필드의 크기
			K = Integer.parseInt(st.nextToken()); // 나무를 벨 수 있는 횟수

			map = new char[N][N];

			// 지도 입력받기
			for (int i = 0; i < N; i++) {
				String line = br.readLine();
				for (int j = 0; j < N; j++) {
					map[i][j] = line.charAt(j);
				}
			}

			total = 0; // 총 리모컨 조작 횟수

			// X 위치에서 BFS 시작
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j] == 'X') {
						total = BFS(i, j);
					}
				}
			}
			System.out.println("#" + tc + " " + total);
		}
	}

	// G: 이동 가능. T: 나무, X: 현재위치, Y: 도착지
	// BFS로 일단 최단거리 찾기
	// 방문체크를 할 때 좌표뿐 아니라 방향, 현재까지 벤 나무의 개수도 함께 고려해야함
	// 큐에 저장할 때는 [행,열, 벤 나무수, 방향, 조작 횟수]
	// 1. 전진  2. 왼90도,  3. 오90도  각 위치에서 3가지모두 시도

	public static int BFS(int i, int j) {
		// 상(0), 우(1), 하(2), 좌(3)
		int[] dx = { -1, 0, 1, 0 };
		int[] dy = { 0, 1, 0, -1 };

		boolean[][][][] visited = new boolean[N][N][K + 1][4]; // 행, 열, 벤 나무 수, 방향

		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] { i, j, 0, 0, 0 }); // 행, 열, 벤 나무 수, 방향, 조작횟수
		visited[i][j][0][0] = true;

		while (!queue.isEmpty()) {
			int[] now = queue.poll();
			int x = now[0];
			int y = now[1];
			int cutTree = now[2];
			int dir = now[3]; // 현재 방향
			int operations = now[4]; // 조작횟수

			// 도착하면 종료
			if (map[x][y] == 'Y') {
				return operations;
			}
			// 1. 전진
			int nx = x + dx[dir];
			int ny = y + dy[dir];

			if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
				// 나무인 경우
				if (map[nx][ny] == 'T') {
					// 나무를 더 벨 수 있고 방문 x인 경우에만 queue에 넣기
					if (cutTree < K && !visited[nx][ny][cutTree + 1][dir]) {
						visited[nx][ny][cutTree + 1][dir] = true;
						queue.offer(new int[] { nx, ny, cutTree + 1, dir, operations + 1 });
					}
				} // 이동 가능한 곳 or 도착지
				else if ((map[nx][ny] == 'G' || map[nx][ny] == 'Y') && !visited[nx][ny][cutTree][dir]) {
					visited[nx][ny][cutTree][dir] = true;
					queue.offer(new int[] { nx, ny, cutTree, dir, operations + 1 });
				}
			}
			// 2. 왼쪽 90도 회전
			int leftDir = (dir + 3) % 4;
			if (!visited[x][y][cutTree][leftDir]) {
				visited[x][y][cutTree][leftDir] = true;
				queue.offer(new int[] { x, y, cutTree, leftDir, operations + 1 });
			}

			// 3. 오른쪽 90도 회전
			int rigthDir = (dir + 1) % 4;
			if (!visited[x][y][cutTree][rigthDir]) {
				visited[x][y][cutTree][rigthDir] = true;
				queue.offer(new int[] { x, y, cutTree, rigthDir, operations + 1 });
			}

		} // 도착하지 못한 경우
		return -1;

	}

}
