import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	static int N;
	static int[][] graph;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int house = 1;
	
	static ArrayList<Integer> result = new ArrayList<>();
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		graph = new int[N][N];
		
		for(int i=0; i<N; i++) {
			String line = br.readLine();
			for(int j=0; j<N; j++) {
				graph[i][j] = line.charAt(j) - '0';
			}
		}
//		System.out.println(Arrays.deepToString(graph));
		
		// 배열을 돌면서 1인 지점이 나타나면 dfs호출
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(graph[i][j] == 1) {
					dfs(i, j);
					result.add(house);
					house = 1;
				}
			}
		}
		Collections.sort(result);
		System.out.println(result.size());
		for(int i=0; i<result.size(); i++) {
			System.out.println(result.get(i));
		}
		
		
		
	}


	private static void dfs(int x, int y) {
		
		// 방문 처리
		graph[x][y] = 0;
		
		for(int k=0; k<4; k++) {
			int nx = x + dx[k];
			int ny = y + dy[k];
			
			if(0 <= nx && nx < N && 0 <= ny &&  ny < N && graph[nx][ny] == 1) {
				dfs(nx, ny);
				house += 1;
			}
		}
	}
}
