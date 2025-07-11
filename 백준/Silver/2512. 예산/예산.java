import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N, need_sum, max_request, budget, left, right, answer, mid, count, total;
	static int[] request;

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine()); // 지방의 수

		// 여러 지방의 예산 요청 입력받기
		request = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		max_request = 0;
		need_sum = 0;
		for (int i = 0; i < N; i++) {
			request[i] = Integer.parseInt(st.nextToken());
			max_request = Math.max(max_request, request[i]);
			need_sum += request[i];
		}
		budget = Integer.parseInt(br.readLine()); // 전체 예산

		// 모든 요청이 배정될 수 있는 경우
		if (need_sum <= budget) {
			System.out.println(max_request);
			
		// 모든 요청이 배정될 수 없는 경우 - 정수 상한액(mid)	
		} else { 

			// 이분탐색
			left = 1;
			right = max_request;
			answer = 0;

			while (left <= right) {
				mid = (left + right) / 2;
				count = N;
				total = 0;

				for (int i = 0; i < N; i++) {
					if (request[i] <= mid) {
						total += request[i];
						count -= 1;
					}
				}

				if ((total + (mid * count)) > budget) {
					right = mid - 1;
					
				} else {
					answer = mid;
					left = mid + 1;
				}
			}

			System.out.println(answer);

		}
	}
}
