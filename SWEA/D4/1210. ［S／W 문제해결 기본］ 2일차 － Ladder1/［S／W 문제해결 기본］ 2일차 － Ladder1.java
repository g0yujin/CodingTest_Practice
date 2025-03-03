import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

class Solution {

	static int T, end;
	static int[][] graph;
	
	public static void main(String[] args) throws Exception{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트케이스만큼 반복
		for(int tc = 1; tc <11; tc++) {
			T = Integer.parseInt(br.readLine());

			// 배열 입력받기
			graph = new int[100][100];
			for(int i=0; i<100; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0; j<100; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
					if(graph[i][j] == 2) {end =  j;}  //end: 끝나는 지점의 y좌표. x좌표는 무조건 99
					
				}
			}
			int result = go(99,end);
			System.out.println("#" + tc + " " + result);
		}	
	}
	
	
	public static int go(int x, int y) {
		
		while(x > 0) {
			graph[x][y] = 2; //방문표시
			
			// 왼쪽확인 - 왼쪽에 길이 있으면 무조건 왼쪽 ㄱㄱ
			if(0 <= y-1 && graph[x][y-1] == 1) {
				y--;  // 왼쪽 이동
				continue;
			}
			
			// 오른쪽 확인 - 오른쪽에 길 있으면 무조건 오른쪽 ㄱㄱ
			if(y+1 <100 && graph[x][y+1] == 1) {
				y++;     // 오른쪽 이동
				continue;
			}
			
			// 좌우로 이동할 수 없다면 위로 이동
			x--;
		}
		return y;
	}
}



	

