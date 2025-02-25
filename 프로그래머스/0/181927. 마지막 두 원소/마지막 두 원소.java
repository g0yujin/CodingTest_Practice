import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int num = num_list.length ;
        int[] answer = new int[num+1];
        
        for(int i=0; i<num; i++){
            answer[i] = num_list[i];
        }
        
        if(num_list[num-1] > num_list[num-2]){
            answer[num] = num_list[num-1] - num_list[num-2];
            
        }else{
            answer[num] = num_list[num-1] * 2;
        }
        return answer;
    }
}