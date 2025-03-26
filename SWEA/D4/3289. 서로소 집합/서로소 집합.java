import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, M, c, a, b;
	static int[] parents;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		// 테스트 케이스 반복
		for(int tc=1; tc<T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());  // 원소의개수
			M = Integer.parseInt(st.nextToken());  // 연산의 개수
			
			StringBuilder sb = new StringBuilder();
			make(); // 각 원소별 집합 만들기
			
			for(int i=0; i<M; i++) {
				st = new StringTokenizer(br.readLine());
				
				c = Integer.parseInt(st.nextToken()); 
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				
				if(c == 0) { // 합집합
					union(a,b);
					
				}else { // 집합에 포함되는지 확인
					if(find(a) == find(b)) {
						sb.append(1);
					}else { sb.append(0);}
				}
			}
			System.out.println("#" + tc + " " + sb);
		}
	}
	
	static void make() {
		parents = new int[N+1];
		
		for(int i=0; i<N; i++) {
			parents[i] = i;
		}
	}
	static int find(int a) { // a가 속한 집합의 대표자 찾기
		
		// 나 자신이 대표자일 때
		if(a == parents[a]) return a;
		
		return parents[a] = find(parents[a]);
		
	}
	
	// 합집합
	static boolean union(int a, int b) {
		
		int aRoot = find(a);
		int bRoot = find(b);
		
		// 만약 두 집합의 대표자가 같다면 
		if(aRoot == bRoot) return false;
		
		parents[bRoot] = aRoot; //합치기
		return true; 			// 유니온 성공
	}
	
}
