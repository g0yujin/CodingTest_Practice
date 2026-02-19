import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;



public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // Please write your code here.
        int current = arr[0];
        ArrayList<Integer> cntList = new ArrayList<>(); 
        int cnt = 0;

        for(int i=1; i<n; i++){
            if(arr[i] == current){
                cnt += 1;
            }
            else{
                cntList.add(cnt);
                cnt = 1;
                current = arr[i];
            }
        }
        System.out.println(Collections.max(cntList));
    }
}