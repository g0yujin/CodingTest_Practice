import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, M, K;
	static int[][] arr;
	static int[][] hap;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());  // 행의 수
		M = Integer.parseInt(st.nextToken());  // 열의 수
		
		arr = new int[N][M];	// 정수 배열
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		K = Integer.parseInt(br.readLine());  // 구해야되는 합의 개수
		
		// i,j,x,y 입력받기
		hap = new int[K][4];
		for(int i=0; i<K; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<4; j++) {
				hap[i][j] = Integer.parseInt(st.nextToken());
			}
		}	
		// 각 합 구하기
		for(int q=0; q<K; q++) {
			int i = hap[q][0] - 1;
			int j = hap[q][1] - 1;
			int x = hap[q][2] - 1;
			int y = hap[q][3] - 1;
			
			int answer = 0;
			
			for(int w=i; w<x+1; w++) {
				for(int e=j; e<y+1; e++) {
					answer += arr[w][e] ;
					
				}
			}		
			System.out.println(answer);
		}
		
		
	}

}
