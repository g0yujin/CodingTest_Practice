import java.util.*;




public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        // Please write your code here.
        int cnt = 1;
        int maxCnt = 1;
        int current = arr[0];

        for(int i=1; i<n; i++){
            if(current == arr[i]){
                cnt += 1;
            }else{
                maxCnt = Math.max(cnt, maxCnt);
                cnt = 1;
                current = arr[i];
            }
        }
                maxCnt = Math.max(cnt, maxCnt);
                System.out.println(maxCnt);
    }
}