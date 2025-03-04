import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {

	static int N, maxScore= 0, flower, maxResult=0;
	static int[][] graph, copy_graph;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());  // 행과 열의 수
		
		// 2차원 배열 입력받기
		graph = new int[N][N];
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				maxScore = Math.max(graph[i][j], maxScore);
			}
		}
		
		// 꽃가루 농도 증가(1~maxScore)
		for(int flower=0; flower<maxScore+1; flower++) {
			// 배열 복사
			copy_graph = new int[N][N];
			for(int q=0; q<N; q++) {
				for(int w=0; w<N; w++) {
					copy_graph[q][w] = graph[q][w];
				}
			}
			
			int result = 0;  // 꽃가루 반응을 보이지 않는 영역의 개수
			
			// 꽃가루 반응을 보이지 않는 영역에서 bfs 탐색 시작
			for(int j=0; j<N; j++) {
				for(int k=0; k<N; k++) {
					if(copy_graph[j][k] > flower) {
						bfs(flower, j, k);
						result += 1;      // bfs가 끝난다 = 꽃가루 반응을 보이지 않는 영역 + 1
					}
				}
			}
			// 꽃가루 반응을 보이지않는 영역의 최대 개수
			maxResult = Math.max(result, maxResult);


			
		}
		System.out.println(maxResult);
		
	}
	
	// 꽃가루 농도보다 높은 곳에서 bfs 탐색 = 꽃가루 반응을 보이지 않는 영역만 탐색하기
	public static void bfs(int flower, int i, int j) {
		ArrayDeque<int[]> queue = new ArrayDeque<>();
		queue.offer(new int[] {i,j});
		copy_graph[i][j] = flower;
		
		while(!queue.isEmpty()) {
			int[] now = queue.poll();
			int x = now[0];
			int y = now[1];
			
			for(int k=0; k<4; k++) {
				
				int nx = x + dx[k];
				int ny = y + dy[k];

				if(0<=nx && nx<N && 0<= ny && ny < N && copy_graph[nx][ny] > flower) {
				    copy_graph[nx][ny] = flower ;  
					queue.offer(new int[] {nx, ny});
				}
			}
		}
		
		
	}

}
