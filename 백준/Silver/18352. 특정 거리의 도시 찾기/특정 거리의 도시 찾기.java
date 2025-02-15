import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, K, X;
	static ArrayList<ArrayList<Integer>> graph;
	static int[] distance;
	
	
	
	public static void main(String[] args)throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken()); // 도시의 개수
		M = Integer.parseInt(st.nextToken()); // 도로의 개수
		K = Integer.parseInt(st.nextToken()); // 거리 정보
		X = Integer.parseInt(st.nextToken()); // 출발 도시의 번호
		
		// graph 초기화 = graph = [[] for _ in range(n+1)]
		graph = new ArrayList<>();
		for(int i=0; i<N+1; i++) {
			graph.add(new ArrayList<>());
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			graph.get(A).add(B);
		}
		// 거리 초기화
		distance = new int[N+1];
		Arrays.fill(distance, -1);  // 거리는 모두 -1f로 초기
		distance[X] = 0;   // 출발 도시는 0
		
		
		// 최단거리가 K인 거리 찾기
		ArrayDeque<Integer> queue = new ArrayDeque<>();
		queue.offer(X);  // 출발 도시 큐에 넣기
		
		while(!queue.isEmpty()) {
			int now = queue.poll();
			for(int next : graph.get(now)) { 
				if(distance[next] == -1) {
					distance[next] = distance[now] + 1;
					queue.offer(next);
				}
				
			}
		}
		boolean found = false;
		for(int i=0; i<N+1; i++) {
			if(distance[i] == K) {
				System.out.println(i);
				found = true;
			}
		}
		if(!found) {
			System.out.println(-1);
		}
	}

}
