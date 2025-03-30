class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        
        int[] result = new int[queries.length];  // 정답을 담을 배열
        
        for(int i=0; i<queries.length; i++){
            int[] temp = queries[i];
            int s = temp[0];
            int e = temp[1];
            int k = temp[2];
            
            int answer = Integer.MAX_VALUE;
            for(int j=s; j<e+1; j++){
                if(arr[j] > k){
                    answer = Math.min(answer, arr[j]);
                }
            }
            if(answer == Integer.MAX_VALUE){
                result[i] = -1;
            }else{
                result[i] = answer;
            }
            
            
        }
        return result;
    }
}