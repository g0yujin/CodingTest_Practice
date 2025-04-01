import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int T, N, total_length, nx = 0, ny = 0;
	static int[][] graph;
	static ArrayList<int[]> core_xy;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int[] length_list;
	static int maxCore, minLength;

	public static void main(String[] args) throws Exception {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    T = Integer.parseInt(br.readLine());
	    
	    for (int tc = 1; tc <= T; tc++) {
	        N = Integer.parseInt(br.readLine());
	        graph = new int[N][N];
	        core_xy = new ArrayList<>();
	        
	        // 맥시노스 입력
	        for (int i = 0; i < N; i++) {
	            StringTokenizer st = new StringTokenizer(br.readLine());
	            for (int j = 0; j < N; j++) {
	                graph[i][j] = Integer.parseInt(st.nextToken());
	                if (graph[i][j] == 1 && i != 0 && i != N-1 && j != 0 && j != N-1) {
	                    core_xy.add(new int[] {i, j});
	                }
	            }
	        }
	        
	        maxCore = 0;
	        minLength = Integer.MAX_VALUE;
	        
	        // 백트래킹으로 탐색
	        backtrack(0, 0, 0);
	        
	        System.out.println("#" + tc + " " + minLength);
	    }
	}

	// index: 현재 처리 중인 코어 인덱스, connected: 현재까지 연결된 코어 수, length: 현재까지의 전선 길이
	public static void backtrack(int index, int connected, int length) {
	    // 모든 코어를 처리했을 때
	    if (index == core_xy.size()) {
	        // 연결된 코어가 더 많거나, 같은 코어 수지만 길이가 더 짧은 경우 업데이트
	        if (connected > maxCore || (connected == maxCore && length < minLength)) {
	            maxCore = connected;
	            minLength = length;
	        }
	        return;
	    }
	    
	    int[] pos = core_xy.get(index);
	    int x = pos[0];
	    int y = pos[1];
	    
	    // 현재 코어를 연결하지 않는 경우
	    backtrack(index + 1, connected, length);
	    
	    // 4방향으로 연결을 시도
	    for (int dir = 0; dir < 4; dir++) {
	        if (canConnect(x, y, dir)) {
	            // 전선 설치하기
	            int wireLength = connect(x, y, dir, 1); // 1: 전선 설치
	            
	            // 다음 코어 처리
	            backtrack(index + 1, connected + 1, length + wireLength);
	            
	            // 백트래킹: 설치했던 전선 제거
	            connect(x, y, dir, 0); // 0: 전선 제거
	        }
	    }
	}

	// dir 방향으로 전선 연결이 가능한지 확인
	public static boolean canConnect(int x, int y, int dir) {
	    int nx = x, ny = y;
	    
	    while (true) {
	        nx += dx[dir];
	        ny += dy[dir];
	        
	        if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
	            return true; // 경계에 도달했으므로 연결 가능
	        }
	        
	        if (graph[nx][ny] != 0) {
	            return false; // 다른 코어나 전선이 있어 연결 불가능
	        }
	    }
	}

	// 전선 설치/제거 및 길이 반환
	public static int connect(int x, int y, int dir, int status) {
	    int count = 0;
	    int nx = x, ny = y;
	    
	    while (true) {
	        nx += dx[dir];
	        ny += dy[dir];
	        
	        if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
	            break; // 경계에 도달
	        }
	        
	        graph[nx][ny] = status; // 1: 전선 설치, 0: 전선 제거
	        count++;
	    }
	    
	    return count; // 설치한 전선 길이 반환
	}
}