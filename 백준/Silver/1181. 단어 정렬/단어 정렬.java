import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	static int N;
	static ArrayList<String> words;
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine()); // 단어의 개수
		
		words = new ArrayList<>();
		for(int i=0; i<N; i++) {
			String now = br.readLine();
			
			// 중복 제거를 위해 있는 것만 넣기
			if(!words.contains(now)) {
				words.add(now);
			}
		}
		
		
		// 길이순 정렬
		Collections.sort(words, (word1, word2) ->{
			if(word1.length() == word2.length()) {
				return word1.compareTo(word2);
			}else {
				return word1.length() - word2.length();
			}
		});
		
		for(String word: words) {
			System.out.println(word);
		}
	}
}
