import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

	static int K;
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		K = Integer.parseInt(br.readLine());
		
		ArrayDeque<Integer> stack = new ArrayDeque<>();
		
		for(int i=0; i<K; i++) {
			int temp = Integer.parseInt(br.readLine());
			if(temp != 0) {
				stack.push(temp);
			}else {
				stack.pop();
			}
		}
		
		int result = 0;
		while(!stack.isEmpty()) {
			result += stack.pop();
		}
		
		System.out.println(result);
	}
}
