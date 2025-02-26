import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
	
	static int T, N, limitCalori;
	static int[] score, calori, selected;
	static int maxScore; 
	
	

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 테스트 케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());  // 재료의 수
			limitCalori = Integer.parseInt(st.nextToken()); // 제한 칼로리
			
			// 재료별 맛과 칼로리 입력받기
			score = new int[N];
			calori = new int[N];
			selected = new int[N];
			
			maxScore = Integer.MIN_VALUE;
			
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				score[i] = Integer.parseInt(st.nextToken());
				calori[i] = Integer.parseInt(st.nextToken());
			}
			
			// 조합 nCr에서 r을 1부터 n개 뽑는 조합 경우의 
			for(int r=1; r<N+1; r++) {
				combi(0, 0, r);
			}
			
			System.out.println("#" + tc + " " + maxScore);
		}
		
		
	}
	
	public static void combi(int cnt, int start, int r) {
		
		// 기저조건: r개만큼 뽑았다면
		if(cnt == r) {
			//칼로리 계산
			int totalCalori = 0;
			int totalScore = 0;
			
			for(int i=0; i<r; i++) {
				totalCalori += calori[selected[i]];
				totalScore += score[selected[i]];
				
			}
			if(totalCalori <= limitCalori) {
				maxScore = Math.max(totalScore, maxScore);
			}
			return;
		}
		
		for(int i=start; i<N; i++) {
			selected[cnt] = i;
			
			combi(cnt+1,i+1, r);
		}
	}
}
