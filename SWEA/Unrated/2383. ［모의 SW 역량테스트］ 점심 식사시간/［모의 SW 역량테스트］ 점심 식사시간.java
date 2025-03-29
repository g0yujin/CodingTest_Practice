import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, st1_length, st1_x, st1_y, st2_length, st2_x, st2_y, cnt_p, time;
	static int[][] room;
	static ArrayList<int[]> people;
	static ArrayList<Integer> st1, st2;
	static int min_time;
	
	
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T = Integer.parseInt(br.readLine());
		// 테스트케이스만큼 반복
		for(int tc=1; tc<T+1; tc++) {
			N = Integer.parseInt(br.readLine()); // 방의 한 변의 길이
			
			// 방의 정보 입력받기
			room = new int[N][N];
			int st_cnt = 0; // 계단의 수
			people = new ArrayList<>();  // 사람 좌표 입력 받기
			
			for(int i=0; i<N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for(int j=0; j<N; j++) {
					room[i][j] = Integer.parseInt(st.nextToken());
					if(room[i][j] > 1) { // 계단 입력받기
						if(st_cnt == 0) {
							// 첫 번째 계단의 길이, x, y좌표
							st1_x = i;
							st1_y = j;
							st1_length = room[i][j];
							st_cnt++;
						}else {
							// 두 번째 계단의 길이, x, y 좌표
							st2_x = i;
							st2_y = j;
							st2_length = room[i][j];
						}
					//사람 좌표 입력 받기
					}else if(room[i][j] == 1) {
						people.add(new int[] {i, j});
					}
					
				}
				
			}
			
			cnt_p = people.size(); // 총 사람수
			min_time = Integer.MAX_VALUE;
			
			combi(); // 부분집합
			
			System.out.println("#" + tc + " " + min_time);
			
		}
		
	}
	
	public static void combi() { // 부분집합
		// 사람이 한 명인 경우
		if(cnt_p == 1) {
	        int[] person = people.get(0);
	        // 두 계단까지의 거리 계산
	        int dist1 = Math.abs(person[0] - st1_x) + Math.abs(person[1] - st1_y);
	        int dist2 = Math.abs(person[0] - st2_x) + Math.abs(person[1] - st2_y);
	        
	        // 가까운 계단 선택
	        int totalTime1 = dist1 + st1_length + 1; // 이동 + 대기(1분) + 계단 내려가기
	        int totalTime2 = dist2 + st2_length + 1; // 이동 + 대기(1분) + 계단 내려가기
	        
	        min_time = Math.min(totalTime1, totalTime2);
	        return; // 더 이상의 계산 필요 없음
		}else {
		    for(int i=0; i<(1<<cnt_p); i++) { 
		        st1 = new ArrayList<>();
		        st2 = new ArrayList<>();
		        
		        for(int j=0; j<cnt_p; j++) {
		            if((i & (1<<j)) != 0) { // st1계단에 가는 경우
		                int[] now = people.get(j);
		                int temp = Math.abs(now[0]-st1_x) + Math.abs(now[1]-st1_y);
		                st1.add(temp);
		            } else { // st2에 간 사람 추가
		                int[] now = people.get(j);
		                int temp = Math.abs(now[0]-st2_x) + Math.abs(now[1]-st2_y);
		                st2.add(temp);
		            }
		        }
		        
		        // 걸리는 시간 정렬
		        Collections.sort(st1);
		        Collections.sort(st2);
		        
		        // 계단 내려가기
		        int current_time = 0;
		        int idx1 = 0;
		        int idx2 = 0;
		        
		        
		        PriorityQueue<Integer> down1 = new PriorityQueue<>();
		        PriorityQueue<Integer> down2 = new PriorityQueue<>();
		        
		        // 모든 사람이 계단을 내려갈 때까지 반복
		        while(idx1 < st1.size() || idx2 < st2.size() || !down1.isEmpty() || !down2.isEmpty()) {
		            
		            
		            // 계단1 내려가기가 완료된 사람 제거
		            while(!down1.isEmpty() && down1.peek() <= current_time) {
		                down1.poll();
		            }
		            
		            // 계단2 내려가기가 완료된 사람 제거
		            while(!down2.isEmpty() && down2.peek() <= current_time) {
		                down2.poll();
		            }
		            
		         // 계단1에 사람 추가 (최대 3명까지)
		            while(idx1 < st1.size() && st1.get(idx1) <= current_time && down1.size() < 3) {
		                // 대기 시간은 계단 도착 시간이 현재 시간과 같을 경우에만 추가
		                int waitTime = (st1.get(idx1) == current_time) ? 1 : 0;
		                down1.add(current_time + st1_length + waitTime);
		                idx1++;
		            }

		            // 계단2에 사람 추가(최대 3명까지)
		            while(idx2 < st2.size() && st2.get(idx2) <= current_time && down2.size() < 3) {
		                // 대기 시간은 계단 도착 시간이 현재 시간과 같을 경우에만 추가
		                int waitTime = (st2.get(idx2) == current_time) ? 1 : 0;
		                down2.add(current_time + st2_length + waitTime);
		                idx2++;
		            }
		            // 모든 사람이 내려갔으면 루프 종료
		            if(idx1 >= st1.size() && idx2 >= st2.size() && down1.isEmpty() && down2.isEmpty()) {
		                break; 
		            }
		            
		            
		            current_time++;
		        }
		        
		    
		        min_time = Math.min(min_time, current_time);
		    }
		}
	}
}
