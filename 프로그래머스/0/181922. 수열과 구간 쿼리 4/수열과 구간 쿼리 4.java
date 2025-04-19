import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for(int q = 0; q < queries.length; q++) {
            int s = queries[q][0]; // 시작 인덱스
            int e = queries[q][1]; // 끝 인덱스
            int k = queries[q][2]; // 나눌 수
            
            for(int i = s; i <= e; i++) {
                // i가 k의 배수인지 확인 (k가 0이면 나눗셈 불가능하므로 별도 처리)
                if(k != 0 && i % k == 0) {
                    arr[i] += 1;
                }
            }
        }
        
        return arr;
    }
}