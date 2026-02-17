import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int answer = 0;
        for(int i=1; i<N+1; i++){
            if(i%2 == 0 || i%3 == 0 || i%5 == 0){
                continue;
            }
            else{
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}