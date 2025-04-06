
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, M;
	static int[][] map;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// 테스트 케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			N = Integer.parseInt(st.nextToken()); // 도시의 크기
			M = Integer.parseInt(st.nextToken()); // 하나의 집이 지불할 수 있는 비용

			// 도시 입력 받기
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int answer = Integer.MIN_VALUE;

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {

					// k=1부터 2*N-2까지
					for (int k = 1; k < (2 * N) - 1; k++) {
						int cost = k * k + (k - 1) * (k - 1); //운영 비용
						int house = 0; // 집의 개수

						for (int r = 0; r < N; r++) {
							for (int c = 0; c < N; c++) {
								// 맨해튼
								if (Math.abs(r - i) + Math.abs(c - j) < k) {
									house += map[r][c];
								}
							}
						}
						if (house * M >= cost) {
							answer = Math.max(answer, house);
						}
					}
				}
			}
			System.out.println("#" + tc + " " + answer);
		}

	}
}
