import java.util.ArrayList;

class Solution {
    public String[] solution(String[] names) {
        int resultSize = names.length%5 == 0? names.length/5 : names.length/5+1;
        String[] result = new String[resultSize];
        
        int idx = 0;
        for(int i=0; i<names.length; i+=5){
            result[idx] = names[i];
            idx ++;
        }
        return result;
    }
}