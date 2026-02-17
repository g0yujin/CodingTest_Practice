import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        System.out.println(N);
        while(N > 0){
            N /= M;
            if(N > 0){
                System.out.println(N);
            }
        }
    }
}
