import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {

	static int T, H, W, N, tank_i, tank_j;
	static char[][] map;
	static char[] input;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		
		// 테스트케이스만큼 반복
		T = Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<T+1; tc++) {
		
			StringTokenizer st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());  // 게임맵 높이
			W = Integer.parseInt(st.nextToken());  // 게임맵 너비
			
			// 게임맵 입력받기
			map = new char[H][W];
			for(int i=0; i<H; i++) {
				String line = br.readLine();
				for(int j=0; j<W; j++) {
					map[i][j] = line.charAt(j);
					
					// 전차의 위치를 tank_i, tank_j에 저장
					if(map[i][j] == '^' || map[i][j] == 'v' || map[i][j] == '>'||map[i][j] == '<') {
						tank_i = i;
						tank_j = j;
					}
				}
			}
			
			N = Integer.parseInt(br.readLine());   // 문자열 길이
			input = new char[N];                   // 사용자가 넣은 입력
			String line = br.readLine();
			for(int i=0; i<N; i++) {
				input[i] = line.charAt(i);
			}
			
			// 전차 위치부터시작하기
			// 각 문자별로 동작 구현하기
			for(int i=0; i<N; i++) {
				char current = input[i];
				
				switch(current) {
					case 'U': U(); break;
					case 'D': D(); break;
					case 'L': L(); break;
					case 'R': R(); break;
					case 'S': S(); break;
				}
			}
			System.out.print("#" + tc + " ");
			
			for(int i=0; i<H; i++) {
				for(int j=0; j<W; j++) {
					System.out.print(map[i][j]);
				}
				System.out.println();
			}
		}
	}
	
	
	
	// 위
	public static void U() {
		
		// 한 칸 위가 평지라면 맵 안이라면
		if(0 <= tank_i-1 && tank_i-1 < H && map[tank_i-1][tank_j] == '.') { 
			map[tank_i-1][tank_j] = '^';   // 한 칸 위로 이동
			map[tank_i][tank_j] = '.';	   // 지나온 자리는 평지
			tank_i -= 1;				   // 전차의 위치 이동
		}else { // 한 칸 위가 평지가 아니라면 = 이동할 수 없다면 
			map[tank_i][tank_j] = '^';  // 전차의 바라보는 방향만 바꾸기
			
		}
	}
	
	
	// 아래
	public static void D() {
		
		// 한 칸 아래가 평지면서 맵 안이라면
		if(0 <= tank_i+1 && tank_i+1 < H && map[tank_i+1][tank_j] == '.') { 
			map[tank_i+1][tank_j] = 'v';   // 한 칸 아래로 이동
			map[tank_i][tank_j] = '.';	   // 지나온 자리는 평지
			tank_i += 1;				   // 전차의 위치 이동
			
		}else { // 한 칸 아래가 평지가 아니라면 = 이동할 수 없다면 
			map[tank_i][tank_j] = 'v';  // 전차의 바라보는 방향만 바꾸기
			
		}
	}
	
	// 왼
	public static void L() {
		// 한 칸 왼쪽이 평지면서 맵 안이라면
		if(0<=tank_j-1  &&  tank_j-1< W && map[tank_i][tank_j-1] == '.') { 
			map[tank_i][tank_j-1] = '<';   // 한 칸 왼쪽으로 이동
			map[tank_i][tank_j] = '.';	   // 지나온 자리는 평지
			tank_j -= 1;				   // 전차의 위치 이동
			
		}else { // 한 칸 아래가 평지가 아니라면 = 이동할 수 없다면 
			map[tank_i][tank_j] = '<';  // 전차의 바라보는 방향만 바꾸기
			
		}
	}
	
	// 오
	public static void R() {
		// 한 칸 오른쪽이 평지면서 맵 안이라면
		if(0<=tank_j+1  &&  tank_j+1<W && map[tank_i][tank_j+1] == '.') { 
			map[tank_i][tank_j+1] = '>';   // 한 칸 오른쪽으로 이동
			map[tank_i][tank_j] = '.';	   // 지나온 자리는 평지
			tank_j += 1;				   // 전차의 위치 이동
			
		}else { // 한 칸 아래가 평지가 아니라면 = 이동할 수 없다면 
			map[tank_i][tank_j] = '>';  // 전차의 바라보는 방향만 바꾸기
			
		}
	}
	
	// 포탄
	public static void S() {
		
		char tank = map[tank_i][tank_j];  // 현재 전차가 바라보고 있는 방향
		
		switch(tank) {
			
			// 전차가 위를 바라볼 때
			case '^':
				for(int i=tank_i-1; i>=0; i--) {
					// 강철벽을 만나면 폭탄 중지
					if(map[i][tank_j] == '#') {break;}
					// 벽돌벽을 만나면 벽 파괴 후 평지로 만들기
					else if(map[i][tank_j] == '*') { map[i][tank_j] = '.'; break;}
					// 그 밖 - 평지 or 물이면 넘어가기
					else {continue;}
				}
				break;
				
			// 전차가 아래를 바라볼 때
			case 'v':
				for(int i=tank_i+1; i<H; i++) {
					// 강철벽을 만나면 폭탄 중지
					if(map[i][tank_j] == '#') {break;}
					// 벽돌벽을 만나면 벽 파괴 후 평지로 만들기
					else if(map[i][tank_j] == '*') { map[i][tank_j] = '.'; break;}
					// 그 밖 - 평지 or 물이면 넘어가기
					else {continue;}
				}
				break;
				
			// 전차가 왼쪽을 바라볼 때
			case '<':
				for(int i=tank_j-1; i>=0; i--) {
					// 강철벽을 만나면 폭탄 중지
					if(map[tank_i][i] == '#') {break;}
					// 벽돌벽을 만나면 벽 파괴 후 평지로 만들기
					else if(map[tank_i][i] == '*') { map[tank_i][i] = '.'; break;}
					// 그 밖 - 평지 or 물이면 넘어가기
					else {continue;}
				}
				break;
				
			// 전차가 오른쪽을 바라볼 때
			case '>':
				for(int i=tank_j+1; i<W; i++) {
					// 강철벽을 만나면 폭탄 중지
					if(map[tank_i][i] == '#') {break;}
					// 벽돌벽을 만나면 벽 파괴 후 평지로 만들기
					else if(map[tank_i][i] == '*') { map[tank_i][i] = '.'; break;}
					// 그 밖 - 평지 or 물이면 넘어가기
					else {continue;}
				}
				break;
		}
		
	}	
}
