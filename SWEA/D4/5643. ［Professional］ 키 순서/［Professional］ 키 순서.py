import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int testCase = 1; testCase <= T; testCase++) {
            int N = Integer.parseInt(br.readLine());  // 학생의 수
            int M = Integer.parseInt(br.readLine());  // 비교 횟수
            
            // 인접 리스트 생성
            List<List<Integer>> graph = new ArrayList<>();
            List<List<Integer>> bigger = new ArrayList<>();
            List<List<Integer>> smaller = new ArrayList<>();
            
            // 리스트 초기화
            for (int i = 0; i <= N; i++) {
                graph.add(new ArrayList<>());
                bigger.add(new ArrayList<>());
                smaller.add(new ArrayList<>());
            }
            
            // 입력 받기
            for (int i = 0; i < M; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph.get(a).add(b);  // a보다 b가 크다
            }
            
            // 자신보다 큰 학생들 찾기 - BFS 사용
            for (int i = 1; i <= N; i++) {
                Deque<Integer> queue = new ArrayDeque<>();
                boolean[] visited = new boolean[N + 1];
                
                queue.add(i);
                visited[i] = true;
                
                while (!queue.isEmpty()) {
                    int now = queue.poll();
                    
                    for (int next : graph.get(now)) {
                        if (!visited[next]) {
                            visited[next] = true;
                            bigger.get(i).add(next);
                            queue.add(next);
                        }
                    }
                }
            }
            
            // 자신보다 작은 학생들 찾기 - 역방향 BFS 대신 관계 활용
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (bigger.get(j).contains(i)) {
                        smaller.get(i).add(j);
                    }
                }
            }
            
            // 순서를 알 수 있는 학생 수 구하기
            int answer = 0;
            for (int i = 1; i <= N; i++) {
                int total = bigger.get(i).size() + smaller.get(i).size();
                if (total == N - 1) {
                    answer++;
                }
            }
            
            System.out.println("#" + testCase + " " + answer);
        }
    }
}