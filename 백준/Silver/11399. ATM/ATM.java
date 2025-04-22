import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	static int N, total, temp;
	static int[] time;
	
	public static void main(String[] args) throws Exception{
		
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		time = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			time[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(time);
		total = 0;
		for(int i=0; i<N; i++) {
			temp += time[i];
			total += temp;
		}
		
		System.out.println(total);
	
	}

}
