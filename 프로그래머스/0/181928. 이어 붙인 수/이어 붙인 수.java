class Solution {
    public int solution(int[] num_list) {
        
        String hol = "";
        String jjak = "";
        
        for(int i=0; i<num_list.length; i++){
            if(num_list[i] % 2 == 1){
                hol += num_list[i];
            }
            else jjak += num_list[i];
        }
        
        
        int hol_int = Integer.parseInt(hol);
        int jjak_int = Integer.parseInt(jjak);
        
        return hol_int + jjak_int;
        
    }
}