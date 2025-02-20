import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		
		// 입력받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] height = new int[9];  // 키 배열
		int sum = 0;
		
		for(int i=0; i<9; i++) {
			height[i] = Integer.parseInt(br.readLine());
			sum += height[i];
		}
		
		//배열 정렬
		Arrays.sort(height);
		
		// sum - 100 이 되는 두 개의 조합 찾기
		int[] delete = new int[2];  // 삭제할 2개를 저장할 배열
		
		for(int i=0; i<9; i++) {
			int temp = height[i];
			for(int j=i+1; j<9; j++) {
				if(temp + height[j] == sum - 100) {
					delete[0] = temp;
					delete[1] = height[j];
					break;
				}
			}
		}
		
		for(int i=0; i<9; i++) {
			if(height[i]!= delete[0] && height[i]!=delete[1]) {
				System.out.println(height[i]);
			}
		}
	}


}
