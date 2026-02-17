import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        String s[] = new String[10];

        for(int i=0; i<10; i++){
            s[i] = sc.next();
        }
        
        for(int i=9; i>-1; i--){
            System.out.print(s[i]);
        }
    }
}