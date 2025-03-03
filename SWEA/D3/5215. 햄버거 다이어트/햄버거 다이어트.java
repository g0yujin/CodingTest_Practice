import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
	static int T, N, L, maxScore;
	static int[] score, calori;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			
			
			// 재료별 점수와 칼로리 입력받기
			score = new int[N];
			calori = new int[N];
			
			for(int i=0; i<N; i++) {
				st = new StringTokenizer(br.readLine());
				score[i] = Integer.parseInt(st.nextToken());
				calori[i] = Integer.parseInt(st.nextToken());
			}
			
			maxScore = 0;
			// 비트마스킹으로 부분조합 2^N반복
			for(int i=0; i<(1<<N); i++) {
				int totalScore = 0;
				int totalCalori = 0;
				
				// j번째 수가 1인지 확인
				for(int j=0; j<N; j++) {
					// j번째 수가 1이면 
					if((i & (1<<j))!= 0) {
						totalScore += score[j];
						totalCalori += calori[j];
					}
				}
				if(totalCalori <= L) {
					maxScore = Math.max(maxScore, totalScore);
				}
			}
			System.out.println("#" + tc + " " + maxScore);
		}
		
		
	}
}