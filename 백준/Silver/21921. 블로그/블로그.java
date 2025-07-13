import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	
	static int N, X;
	static ArrayList<Integer> visited, sumArr;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
				
		visited = new ArrayList<>();
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<N; i++) {
			visited.add(Integer.parseInt(st.nextToken()));
		}
		
		// 처음 윈도우 계산
		int windowSum = 0;
		for(int i=0; i<X; i++) {
			windowSum += visited.get(i);
		}
		sumArr = new ArrayList<>();
		sumArr.add(windowSum);
		
		
		// 윈도우 시작
		int max_visited = windowSum;
		for(int i=X; i<N; i++) {
			windowSum += visited.get(i) - visited.get(i-X);
			sumArr.add(windowSum);
			max_visited = Math.max(max_visited, windowSum);
			
		}
		
		if(max_visited > 0) {
			System.out.println(max_visited);
			int count = 0;
			for(int i=0; i<sumArr.size(); i++) {
				if(sumArr.get(i) == max_visited) {
					count += 1;
				}
			}
			System.out.println(count);
		}else {
			System.out.println("SAD");
		}

		
	}
}
