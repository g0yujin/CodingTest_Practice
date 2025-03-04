import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
class Solution {
     
    static int T, N;
    static String S;
    static int[][] graph, result;
     
    public static void main(String[] args) throws Exception{
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         
        //테스트케이스만큼 반복
        T = Integer.parseInt(br.readLine());
        for(int tc=1; tc<T+1; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());    // 타일 크기 N*N
            S = st.nextToken();   // 타일 이동 방향
             
            //타일 입력받기
            graph = new int[N][N];
            for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j=0; j<N; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }
             
            // 결과 배열 초기화
            result = new int[N][N];
             
            // 타일 이동 방향에 따른 함수 실행
            switch(S) {
            case "left":
                left();
                break;
                 
            case "right":
                right();
                break;
                 
            case "up":
                up();
                break;
                 
            case "down":
                down();
                break;
            }
             
            // 결과 출력
            System.out.println("#" + tc);
            for(int i=0; i<N; i++) {
                for(int j=0; j<N; j++) {
                    System.out.print(result[i][j] + " ");
                }
                System.out.println();
            }
        }
    }
     
    public static void left() {
        for(int i=0; i<N; i++) { 
            int[] row = new int[N];
            // 현재 행 복사
            for(int j=0; j<N; j++) {
                row[j] = graph[i][j];
            }
             
            int idx = 0;
            int[] temp = new int[N];
             
            // 0이 아닌 숫자들만 왼쪽으로 모으기
            for(int j=0; j<N; j++) {
                if(row[j] != 0) {
                    temp[idx++] = row[j];
                }
            }
             
            // 같은 숫자 합치기
            for(int k=0; k<idx-1; k++) {
                if(temp[k] == temp[k+1]) {
                    temp[k] *= 2;
                    temp[k+1] = 0;
                }
            }
             
            // 다시 0이 아닌 숫자들을 왼쪽으로 모으기
            int[] finish = new int[N];
            idx = 0;
            for(int l=0; l<N; l++) {
                if(temp[l] != 0) {
                    finish[idx++] = temp[l]; 
                }
            }
             
            // 결과 저장
            result[i] = finish;
        }
    }
     
    public static void right() {
        for(int i=0; i<N; i++) {
            int[] row = new int[N];
            // 현재 행 복사 (역순)
            for(int j=0; j<N; j++) {
                row[j] = graph[i][N-1-j];
            }
             
            int idx = 0;
            int[] temp = new int[N];
             
            // 0이 아닌 숫자들만 왼쪽으로 모으기
            for(int j=0; j<N; j++) {
                if(row[j] != 0) {
                    temp[idx++] = row[j];
                }
            }
             
            // 같은 숫자 합치기
            for(int k=0; k<idx-1; k++) {
                if(temp[k] == temp[k+1]) {
                    temp[k] *= 2;
                    temp[k+1] = 0;
                }
            }
             
            // 다시 0이 아닌 숫자들을 왼쪽으로 모으기
            int[] finish = new int[N];
            idx = 0;
            for(int l=0; l<N; l++) {
                if(temp[l] != 0) {
                    finish[idx++] = temp[l]; 
                }
            }
             
            // 결과 저장 (역순)
            for(int j=0; j<N; j++) {
                result[i][j] = finish[N-1-j];
            }
        }
    }
     
    public static void up() {
        for(int j=0; j<N; j++) {
            int[] col = new int[N];
            // 현재 열 복사
            for(int i=0; i<N; i++) {
                col[i] = graph[i][j];
            }
             
            int idx = 0;
            int[] temp = new int[N];
             
            // 0이 아닌 숫자들만 위로 모으기
            for(int i=0; i<N; i++) {
                if(col[i] != 0) {
                    temp[idx++] = col[i];
                }
            }
             
            // 같은 숫자 합치기
            for(int k=0; k<idx-1; k++) {
                if(temp[k] == temp[k+1]) {
                    temp[k] *= 2;
                    temp[k+1] = 0;
                }
            }
             
            // 다시 0이 아닌 숫자들을 위로 모으기
            int[] finish = new int[N];
            idx = 0;
            for(int l=0; l<N; l++) {
                if(temp[l] != 0) {
                    finish[idx++] = temp[l]; 
                }
            }
             
            // 결과 저장
            for(int i=0; i<N; i++) {
                result[i][j] = finish[i];
            }
        }
    }
     
    public static void down() {
        for(int j=0; j<N; j++) {
            int[] col = new int[N];
            // 현재 열 복사 (역순)
            for(int i=0; i<N; i++) {
                col[i] = graph[N-1-i][j];
            }
             
            int idx = 0;
            int[] temp = new int[N];
             
            // 0이 아닌 숫자들만 위로 모으기
            for(int i=0; i<N; i++) {
                if(col[i] != 0) {
                    temp[idx++] = col[i];
                }
            }
             
            // 같은 숫자 합치기
            for(int k=0; k<idx-1; k++) {
                if(temp[k] == temp[k+1]) {
                    temp[k] *= 2;
                    temp[k+1] = 0;
                }
            }
             
            // 다시 0이 아닌 숫자들을 위로 모으기
            int[] finish = new int[N];
            idx = 0;
            for(int l=0; l<N; l++) {
                if(temp[l] != 0) {
                    finish[idx++] = temp[l]; 
                }
            }
             
            // 결과 저장 (역순)
            for(int i=0; i<N; i++) {
                result[N-1-i][j] = finish[i];
            }
        }
    }
}
