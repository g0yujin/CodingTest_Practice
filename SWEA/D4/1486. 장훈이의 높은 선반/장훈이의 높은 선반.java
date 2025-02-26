import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {

	static int T, N, B;
	static int[] height, selected;
	static int minHeight;
	
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 테스트 케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken()); // 점원 수
			B = Integer.parseInt(st.nextToken()); // 선반 높이
			
			// 점원들의 키 배열 입력받기
			height = new int[N];
			st = new StringTokenizer(br.readLine());
			for(int i=0; i<N; i++) {
				height[i] = Integer.parseInt(st.nextToken());
			}
			
			minHeight = Integer.MAX_VALUE;
			selected = new int[N];
			
			//nCr의 모든 부분집합
			for(int r=1; r<N+1; r++) {
				combi(0, 0, r);
			}
			System.out.println("#" + tc + " " + (minHeight - B));
		}
	}
	
	public static void combi(int cnt, int start, int r) {
		
		// 기저조건 : r개 뽑았다면
		if(cnt == r) {
			
			// 뽑은 키들의 합 계산하기
			int sum = 0;
			for(int i=0; i<r; i++) {
				sum += height[selected[i]];
			}
			if(sum >= B) {
				minHeight = Math.min(minHeight, sum);
			}
			return;
		}
		for(int i=start; i<N; i++) {
			
			selected[cnt] = i;
			
			combi(cnt+1, i+1, r);
		}
	}
}
