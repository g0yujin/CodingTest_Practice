import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

	static int T;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		T= Integer.parseInt(br.readLine());
		
		for(int tc=1; tc<T+1; tc++) {  // 테스트케이스만큼 반복
			String ps = br.readLine();
			ArrayDeque<Character> queue = new ArrayDeque<>();
			int left = 0;
			int right = 0;
			
			for(int i=0; i<ps.length(); i++) {
				if(ps.charAt(i) == '(') {
					queue.offer('(');
					left += 1;
					
				}else if(ps.charAt(i) == ')') {
					if(!queue.isEmpty()) { // 왼쪽 괄호가 queue에 있다면
						queue.poll();
						right += 1;
					}
				}
			}
			
			if(queue.isEmpty() && left==right && left+right == ps.length()) {
				System.out.println("YES");
			}else {
				System.out.println("NO");
			}
		}
	}
}
