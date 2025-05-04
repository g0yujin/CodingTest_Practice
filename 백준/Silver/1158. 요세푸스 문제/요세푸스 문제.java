import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    static int N, K;

    public static void main(String[] args)throws Exception{
     
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());

            ArrayList<Integer> list = new ArrayList<>();

            for(int i=1; i<=N; i++) {
                list.add(i);
            }
            
            StringBuilder sb = new StringBuilder();
            sb.append("<");
            int index = 0;
            
            while(list.size() > 0) {
            	index = (index + K - 1) % list.size();
            	
            	sb.append(list.remove(index));
            	
            	if(list.size()>0) {
            		sb.append(", ");
            	}
            }
            
            sb.append(">");
            System.out.println(sb.toString());
            
       
    }
}