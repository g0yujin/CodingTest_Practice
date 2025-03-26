import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int N, S, from, to, now, maxNode;
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 10개의 테스트케이스
		for(int tc=1; tc<11; tc++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			S = Integer.parseInt(st.nextToken());
			
			
			// 인접리스트 101 *101
			graph = new ArrayList[101];
			for(int i=1; i<101; i++) {
				graph[i] = new ArrayList<>();
			}
			
			// 인접 리스트 입력받기
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N/2; i++) {
				from = Integer.parseInt(st.nextToken());
				to = Integer.parseInt(st.nextToken());
				graph[from].add(to);
			}
			visited = new boolean[101];
			// 시작점에서 BFS 시작
			
			BFS(S);
			System.out.println("#" + tc + " " + maxNode);
		}
	}

	public static void BFS(int num) {
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		
		visited[num] = true;
		queue.offer(num);
		
		// 큐가 빌 때까지 실행
		while(!queue.isEmpty()) {
			maxNode = 0;
			int levelSize = queue.size();
			for(int i=0; i<levelSize; i++) {
				
				int now = queue.poll();
				maxNode = Math.max(maxNode, now);
				
				for(int next : graph[now]) {
					if(!visited[next]) {
						visited[next] = true;
						queue.offer(next);
					}
				}
				
			}
		}
 	}
}


