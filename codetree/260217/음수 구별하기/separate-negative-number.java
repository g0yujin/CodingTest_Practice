import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        
        if(a<0){
            System.out.println(a);
            System.out.println("minus");
        }else{
            System.out.println(a);
        }
    }
}