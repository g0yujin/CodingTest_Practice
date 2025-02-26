import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


class Solution {

	static int T, N;
	static int[][] synergy;
	static int[] A, B;
	static int minDiff;
	
	
	public static void main(String[] args) throws Exception{
		
		// 입력받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		
		// 테스트케이스 개수만큼 반복
		for(int tc=1; tc<T+1; tc++) {
			N = Integer.parseInt(br.readLine());  // 식재료개
			synergy = new int[N+1][N+1];
			
			// 시너지 입력
			for(int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					synergy[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			//음식별 식재료 배열 선언
			A = new int[N/2];
			B = new int[N/2];
			
			minDiff = Integer.MAX_VALUE;
			// 조합 시작
			combi(0,0);
			
			//결과 출력
			System.out.println("#" + tc + " " + minDiff);
		}
	}
	
	
	// 조합으로 A음식의 식재료 선택하기
	public static void combi(int cnt, int start) { // start:탐색 시작 인덱스, r: 뽑을개수
		
		// 기저조건 : N/2개를 모두 뽑았다면
		if(cnt == N/2) {
			
			// B 배열 채우기
			fillB();
			// 시너지 계산하고 최소값 갱신
			int diff = calcSy();
			minDiff = Math.min(minDiff, diff);
			
			return;
			
		}
		// start부터 N-1까지 탐색
		for(int i=start; i<N; i++) {
			// 현재 인덱스에 i를 선택
			A[cnt] = i;
			
			// 다음 단계 진행
			combi(cnt+1, i+1);
		}
	}
	
	//A에서 식재료 선택 후 남은 식재료로 B 채우기
	public static void fillB() {
		
		boolean[] selected = new boolean[N];
		
		for(int i=0; i<A.length; i++) {
			selected[A[i]] = true;
		}
		
		int idx = 0;
		for(int i=0; i<N; i++) {
			if(!selected[i]) {
				B[idx++] = i;
			}
		}
	}
	
	
	// 시너지 계산하기
	public static int calcSy() {
		int sumA = 0;
		int sumB = 0;
		
		for(int i=0; i<N/2; i++) {
			for(int j=0; j<N/2; j++) {
				if(i!=j) {
					sumA += synergy[A[i]][A[j]];
					sumB += synergy[B[i]][B[j]];
				}
			}
		}
		
		// 두 팀의 시너지 차이의 절댓값 반환
        return Math.abs(sumA - sumB);
	}
	
}
