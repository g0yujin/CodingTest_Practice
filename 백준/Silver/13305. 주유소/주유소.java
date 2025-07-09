import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, cheap, need;
	static int[] road, oil;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
	
		N = Integer.parseInt(br.readLine());
		
		road = new int[N-1];
		StringTokenizer st = new StringTokenizer(br.readLine());		
		for(int i=0; i<N-1; i++) {
			road[i] = Integer.parseInt(st.nextToken());
		}
		
		oil = new int[N];
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			oil[i] = Integer.parseInt(st.nextToken());
		}
		
		need = 0;
		cheap = Integer.MAX_VALUE;
		for(int i=0; i<N-1; i++) {
			cheap = Math.min(cheap, oil[i]);
			need += cheap * road[i];
			
		}
		
		System.out.println(need);
	}
}
