import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	
	static class Edge implements Comparable<Edge>{
		int from, to, weight;

		public Edge(int from, int to, int weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}
		
		@Override
		public int compareTo(Edge o) {
			return Integer.compare(this.weight, o.weight);
		}
	}
	
	
	static int T, V, E;
	static Edge[] edgeList;
	static int[] parents;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		
		// 테스트케이스만큼 반복
		for(int tc=1; tc<T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			V = Integer.parseInt(st.nextToken()); // 정점의 개수
			E = Integer.parseInt(st.nextToken()); // 간선의 개수
			
			
			// 간선 정보 입력받기
			edgeList = new Edge[E];
			for(int i=0; i<E; i++) {
				st = new StringTokenizer(br.readLine());
				
				int A = Integer.parseInt(st.nextToken());
				int B = Integer.parseInt(st.nextToken());
				int C = Integer.parseInt(st.nextToken());
				
				edgeList[i] = new Edge(A, B, C);
			}
			
			make();
			
			// 간선 정렬
			Arrays.sort(edgeList);
			
			long result = 0; // 총 가중치
			int cnt = 0; 	// 간선의 개수
			
			for(Edge edge : edgeList) {
				if(union(edge.from, edge.to)) { // 두 정점이 속한 트리를 합칠 수 있다면
					
					result += edge.weight;
					
					 // 기저 조건
					if(++cnt == V-1) {
						break;
					}
				}
			}
			System.out.println("#" + tc + " " + result);
		}
	}
	// 각 원소를 대표자로 하는 집합 만들기
	static void make() {
		parents = new int[V+1];
		
		for(int i=1; i<V+1; i++) {
			parents[i] = i;
		}
	}
	
	// 대표자 찾기
	static int find(int a) {
		
		if(a == parents[a]) return a;
		return parents[a] = find(parents[a]);
	}
	
	
	// 합치기
	static boolean union(int a, int b) {
		
		int aRoot = find(a);
		int bRoot = find(b);
		
		if(aRoot == bRoot) return false;
		
		parents[bRoot] = aRoot;
		return true;
	}
}
