import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

class Solution {

	static int T, N;
	static int[][] rooms;
	static int[][] move;
	static ArrayList<Integer> result;
	
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	
	static int maxValue;
	
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트 케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
		
			N = Integer.parseInt(br.readLine()); 
			
			// 방 숫자 입력받기
			rooms = new int[N][N];  
			for(int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					rooms[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			move = new int[N][N];  // 이동가능한 방의 개수
			maxValue = Integer.MIN_VALUE;
			result = new ArrayList<>();
			
			// 모든 방에서 bfs 실행
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					bfs(i, j);
				}
			}
			
			// 가장 많이 이동할 수 있는 방을 result에 저장
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(move[i][j] == maxValue) {
						result.add(rooms[i][j]);
					}
				}
			}
			int min = Collections.min(result);
//			System.out.println(Arrays.deepToString(move));
			System.out.println("#"+ tc + " " + min + " " + maxValue);
		}
		
	}


	public static void bfs(int i, int j) {
		
		int cnt = 1; //이동 가능한 방의 개수
		
		ArrayDeque<int[]> queue = new ArrayDeque<>(); 
		queue.offer(new int[] {i, j});
		
		while(!queue.isEmpty()) {
			int[] now = queue.poll();
			int x = now[0];
			int y = now[1];
			
			for(int k=0; k<4; k++){
				int nx = x + dx[k];
				int ny = y + dy[k];
				
				if(0<= nx && nx< N && 0<= ny && ny<N && rooms[nx][ny] == rooms[x][y]+1) {
					queue.offer(new int[]{nx, ny});
					cnt += 1;
					
				}
			}
		}
		move[i][j] = cnt;
		maxValue = Math.max(cnt, maxValue);
				
	}
	
	
}
