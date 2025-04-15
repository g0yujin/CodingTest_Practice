import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int T, M, N, K, answer;
	static int[][] map;
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken()); // 배추밭 가로길이
			N = Integer.parseInt(st.nextToken()); // 배추밭 세로길이
			K = Integer.parseInt(st.nextToken()); // 배추가 심어져있는 위치의 개수
			
			map = new int[N][M];
			// 배추위치
			for(int b=0; b<K; b++) {
				st = new StringTokenizer(br.readLine());
				int A = Integer.parseInt(st.nextToken());
				int B = Integer.parseInt(st.nextToken());
				map[B][A] = 1;
			}
			answer = 0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					if(map[i][j] == 1) {
						DFS(i,j);
						answer += 1;
					}
					
				}
			}
			System.out.println(answer);
		}
	}
	
	public static void DFS(int i, int j) {
		map[i][j] = 0; // 방문처리
		
		for(int k=0; k<4; k++) {
			int nx = i + dx[k];
			int ny = j + dy[k];
			
			if(nx>=0 && nx<N && ny>=0 && ny<M && map[nx][ny] == 1) {
				DFS(nx, ny);
			}
		}
	}
}
