import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
	
	
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for(int test_case=1; test_case<=10; test_case++) {
            int N = Integer.parseInt(br.readLine());
            String brackets = br.readLine();
            
            int result = isValid(brackets) ? 1 : 0;
            System.out.println("#" + test_case + " " + result);
        }
    }
    
    public static boolean isValid(String brackets) {
       ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for(int i=0; i<brackets.length(); i++) {
            char current = brackets.charAt(i);

            // 총 괄호의 수가 홀수이면 false 
            if(brackets.length() % 2 == 1) { return false;}
           
            
            
            if(current == '(' || current == '[' || current == '{' || current == '<') {
                stack.push(current);
            } else {
                if(stack.isEmpty()) {
                    return false;
                }
                
                char top = stack.pop();
                if((current == ')' && top != '(') || 
                   (current == ']' && top != '[') ||
                   (current == '}' && top != '{') ||
                   (current == '>' && top != '<')) {
                    return false;
                }
            }
        }
        
        return stack.isEmpty();
    }
}