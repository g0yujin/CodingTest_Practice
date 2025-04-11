import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Solution {

	static int T;
	static int[][] map;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static boolean[][] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 10번의 테스트케이스
		for (int tc = 1; tc < 11; tc++) {

			T = Integer.parseInt(br.readLine());
			
			map = new int[16][16];
			for (int i = 0; i < 16; i++) {
				String line = br.readLine();
				for (int j = 0; j < 16; j++) {
					map[i][j] = line.charAt(j) - '0';
				}
			}
			visited = new boolean[16][16];
			System.out.println("#" + T + " " + BFS(1,1));

		}
	}

	public static int BFS(int i, int j) {
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] { i, j });
		
		while (!queue.isEmpty()) {
			int[] now = queue.poll();
			int x = now[0];
			int y = now[1];

			if (x == 13 && y == 13) {
				return 1;
			}

			for (int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];

				if (0 <= nx && nx < 16 && 0 <= ny && ny < 16 && (map[nx][ny] == 0 || map[nx][ny] == 3)&& visited[nx][ny] == false) {
					
					queue.offer(new int[] {nx, ny});
					visited[nx][ny] = true;
				}
			}
		}
		return 0;
	}
}
