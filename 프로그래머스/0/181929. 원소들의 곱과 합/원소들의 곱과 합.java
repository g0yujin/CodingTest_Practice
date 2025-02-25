class Solution {
    public int solution(int[] num_list) {
        int gop = num_list[0];
        int hapje = num_list[0];
        
        for(int i=1; i<num_list.length; i++){
            gop *= num_list[i];
            hapje += num_list[i];
        }
        
        if(gop < hapje*hapje) {return 1;}
        else { return 0; }
    }
}