import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int R, C, count;
	static char[][] graph;
	static int[] dx = {-1, 0, 1}; // 오위, 오, 오아
	static int[] dy = {1, 1, 1};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken()); // 행의 수
		C = Integer.parseInt(st.nextToken()); // 열의 수
		
		// 격자 입력 받기 R*C
		graph = new char[R][C];
		for(int i=0; i<R; i++) {
			String line = br.readLine();
			for(int j=0; j<C; j++) {
				graph[i][j] = line.charAt(j);
			}
		}
		
		// 첫째 열에서 BFS 시작
		for(int i=0; i<R; i++) {
			if(DFS(i, 0)){
				count++;
			}
		}
		System.out.println(count);
		
	}

	public static boolean DFS(int x, int y) {
		
		// 마지막 열에 도달하면 성공
		if(y == C-1) {
			return true;
		}
		
		for(int k=0; k<3; k++) {
			
			int nx = x + dx[k];
			int ny = y + dy[k];
			
			if(0 <= nx && nx<R && 0<=ny && ny<C && graph[nx][ny] == '.') {
				// 지나간 곳 표시
				graph[nx][ny] = 'x';
				
				if(DFS(nx, ny)) {
					return true;
				}
			}
		}
		return false;
		
	}
	
}
