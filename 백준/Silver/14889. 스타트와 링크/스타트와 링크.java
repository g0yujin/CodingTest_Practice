
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	 
	static int N, mincha;
	static int[][] graph;
	static boolean[] selected;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
		graph = new int[N][N];
		
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			
			}
		}
		selected = new boolean[N];
		mincha = Integer.MAX_VALUE;
		combi(0,0);
		
		System.out.println(mincha);
	}
	

	
	// 조합
	public static void combi(int cnt, int start) {
	    // 기저 조건 : r개를 모두 뽑았다면
	    if(cnt == N/2) {
	        // 능력치 직접 계산 방식으로 변경
	        int start_ability = 0;
	        int link_ability = 0;
	        
	        for(int i=0; i<N; i++) {
	            for(int j=0; j<N; j++) {
	                if(i == j) continue; // 자기 자신은 제외
	                
	                if(selected[i] && selected[j]) {
	                    start_ability += graph[i][j];
	                } else if(!selected[i] && !selected[j]) {
	                    link_ability += graph[i][j];
	                }
	            }
	        }
	        
	        mincha = Math.min(mincha, Math.abs(start_ability - link_ability));
	        return;
	    }
	    
	    // start부터 N-1까지 탐색
	    for(int i=start; i<N; i++) {
	        // 현재 인덱스 i를 선택
	        selected[i] = true;
	        
	        // 다음 단계로 진행
	        combi(cnt+1, i+1);
	        
	        // 백트래킹
	        selected[i] = false;
	    }
	}
}
