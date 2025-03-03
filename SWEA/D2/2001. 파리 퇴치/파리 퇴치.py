import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
	static int T, N, M;
	static int[][] graph;
	static int maxFly; 

	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트케이스만큼 반복
		T = Integer.parseInt(br.readLine());
	
		for(int tc=1; tc<T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			maxFly = Integer.MIN_VALUE;
			
			// 배열 입력받기
			graph = new int[N][N];
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			getMaxFly();
			System.out.println("#" + tc + " " + maxFly);
		}
		
	}
	
	public static void getMaxFly() {
		
		
		// 파리채가 배열의 범위를 벗어나지 않도록
		for(int i=0; i<=N-M; i++) {
			for(int j=0; j<=N-M; j++) {
				int sum = 0;
				
				for(int x=0; x<M; x++) {
					for(int y=0; y<M; y++){
						sum += graph[i+x][j+y];
					}
				}
				maxFly = Math.max(maxFly, sum);
			}
		}
	}
}
