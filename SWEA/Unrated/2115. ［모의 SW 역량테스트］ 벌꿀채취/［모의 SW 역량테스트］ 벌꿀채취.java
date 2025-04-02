import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, M, C, answer;
	static int[][] honey;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc < T + 1; tc++) {
			answer = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());

			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());

			honey = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					honey[i][j] = Integer.parseInt(st.nextToken());

				}
			}
			// 첫 번째 일꾼의 벌통
			for (int r1 = 0; r1 < N; r1++) {
				for (int c1 = 0; c1 < N - M + 1; c1++) {
					// 두 번째 일꾼의 벌통
					for (int r2 = 0; r2 < N; r2++) {
						for (int c2 = 0; c2 < N - M + 1; c2++) {

							// 벌통이 겹치면 넘어가기
							if (r1 == r2 && c1 + M > c2)
								continue;

							int profit1 = getHoney(r1, c1);
							int profit2 = getHoney(r2, c2);
							answer = Math.max(answer, profit1 + profit2);

						}
					}
				}
			}
			System.out.println("#" + tc + " " + answer);
		}

	}

	public static int getHoney(int r, int c) {
		int[] honeys = new int[M];
		// 선택된 벌통 M개 배열에 저장
		for (int i = 0; i < M; i++) {
			honeys[i] = honey[r][c + i];
		}

		int maxProfit = 0;
		// 2^M개의 모든 부분집합에 대해 확인
		for (int i = 1; i < (1 << M); i++) {
			int sum = 0; 	// 꿀의 양 합계
			int profit = 0; // 수익

			
			for (int j = 0; j < M; j++) {
				if ((i & (1 << j)) != 0) { 
					sum += honeys[j]; 		
					profit += honeys[j] * honeys[j]; 
				}
			}

			// 꿀의 양이 C 이하인 경우만 이익 계산
			if (sum <= C) {
				maxProfit = Math.max(maxProfit, profit);
			}
		}

		return maxProfit;
	}
}
