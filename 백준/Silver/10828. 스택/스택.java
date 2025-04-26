import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	static int N;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		ArrayDeque<Integer> stack = new ArrayDeque<>();
		for(int i=0; i<N; i++) {
			String line = br.readLine();
			String[] part = line.split(" ");
			String order = part[0];
				
			switch(order) {
			
			case "push":
				int num = Integer.parseInt(part[1]);
				stack.push(num);
				break;
			
			
			case "pop":
				
				if(stack.isEmpty()) {
					System.out.println(-1);
				}else {
					int now = stack.pop();
					System.out.println(now);
				}
				break;
			
			case "size":
				System.out.println(stack.size());
				break;
				
			case "empty":
				if(stack.isEmpty()) {
					System.out.println(1);
				}else {
					System.out.println(0);
				}
				break;
				
			case "top":
				if(stack.isEmpty()) {
					System.out.println(-1);
				}else {
					System.out.println(stack.peek());
				}
				break;
			}
		}
	}
}
