import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    static int T, N, K, maxHeight;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0}; // 상하좌우
    static int[] dy = {0, 0, -1, 1};
    static int maxLen; // 최대 등산로 길이

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        //테스트케이스만큼 반복
        for(int tc=1; tc<=T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // 지도 한 변의 길이
            K = Integer.parseInt(st.nextToken()); // 최대 공사 가능 깊이

            maxHeight = 0; // 가장 높은 봉우리
            maxLen = 0; // 최대 등산로 길이 초기화

            // 부지 입력받기
            map = new int[N][N];
            
            for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j=0; j<N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                    maxHeight = Math.max(maxHeight, map[i][j]);
                }
            }

            // 가장 높은 봉우리에서 dfs시작
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    if(map[i][j] == maxHeight) {
                        visited = new boolean[N][N]; // 각 시작점마다 방문 배열 초기화
                        visited[i][j] = true;
                        dfs(i, j, 1, false); // 시작 지점, 길이 1, 아직 공사 안함
                        visited[i][j] = false;
                    }
                }
            }
            
            System.out.println("#" + tc + " " + maxLen);
        }
    }
    
    // dfs 함수: (x,y) 좌표, 현재까지의 등산로 길이, 공사 사용 여부
    static void dfs(int x, int y, int length, boolean used) {
        // 현재 등산로 길이가 최대값보다 크면 갱신
        maxLen = Math.max(maxLen, length);
        
        // 상하좌우 4방향 탐색
        for(int d=0; d<4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            // 범위 체크 및 방문 체크
            if(nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny]) {
                continue;
            }
            
            // 현재 위치보다 낮은 곳이면 그냥 이동
            if(map[nx][ny] < map[x][y]) {
                visited[nx][ny] = true;
                dfs(nx, ny, length + 1, used);
                visited[nx][ny] = false;
            }
            // 현재 위치보다 높거나 같은 곳이면서 아직 공사를 하지 않았다면
            else if(!used) {
                // 최대 K만큼 깎아서 현재 위치보다 낮아질 수 있는지 확인
                int diff = map[nx][ny] - map[x][y] + 1; // 최소 이 정도는 깎아야 지나갈 수 있음
                if(diff <= K) { // 공사 가능한 범위 내라면
                    int original = map[nx][ny]; // 원래 높이 저장
                    map[nx][ny] = map[x][y] - 1; // 현재 위치보다 1 낮게 깎음
                    visited[nx][ny] = true;
                    dfs(nx, ny, length + 1, true); // 공사 사용 표시
                    visited[nx][ny] = false;
                    map[nx][ny] = original; // 원래 높이로 복원
                }
            }
        }
    }
}