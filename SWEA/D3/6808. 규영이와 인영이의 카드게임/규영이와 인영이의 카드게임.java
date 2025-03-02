import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {

	static int T, win, lose;
	static int[] gyu, in, numbers;
	static boolean[] exists, isSelected;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 테스트 케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		for(int tc=1; tc<T+1; tc++) {
			
			gyu = new int[9];
			numbers = new int[9];
			
			//규영이의 카드 입력받기
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int i=0; i<9; i++) {
				gyu[i] = Integer.parseInt(st.nextToken());
			}
			
			//인영이의 카드
			exists = new boolean[19]; // 인덱스 1~18까지 사용 
			// 규영이가 가진 카드의 숫자들을 true 표시
			for(int g: gyu) {
				exists[g] = true;
			}
			
			int idx = 0;
			for(int i=1; i<19; i++) {
				if(!exists[i]) {
					numbers[idx++] = i;
				}
			}
			
			// 순열
			in = new int[9]; // 순열로 선택된 수 = 인영이가 낼 카드
			isSelected = new boolean[9]; //쓰인 수
			win = 0;
			lose = 0;
					
			permu(0);
			System.out.println("#" + tc + " " + win + " " + lose);
			
		}
	}
	// cnt: 몇 번째 자리인지
	// i : 어떤 숫자를 선택할지
	// 순열 함수
	public static void permu(int cnt) {
		if(cnt == 9) {
			calc();
			return;
		}
		
		for(int i=0; i<9; i++) {
			if(isSelected[i]) continue; // 이미 선택된 요소는 스킵
			
			in[cnt] = numbers[i];
			isSelected[i] = true;
			permu(cnt+1);
			isSelected[i] = false;
		}
	}
	
	
	// 누가 이기는지 계산하는 함수
	public static void calc() {
		int gyu_score = 0;
		int in_score = 0;
		
		for(int i=0; i<9; i++) {
			if(gyu[i] > in[i]) {gyu_score+= gyu[i]+in[i];} // 규영이가 낸 카드가 더 큰 경우
			else if(in[i] > gyu[i]) {in_score += gyu[i]+in[i];} // 규영이가 낸 카드가 더 작은 경우
		}
		if(gyu_score > in_score) {win += 1;}  // 규영이가 이기는 경우
		else if(gyu_score < in_score) {lose += 1;} // 규영이가 지는 경우
		
	}
}
