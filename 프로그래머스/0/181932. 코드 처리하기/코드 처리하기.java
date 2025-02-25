class Solution {
    public String solution(String code) {
        int mode = 0;
        String ret = "";
        for(int i=0; i<code.length(); i++) {
            char temp = code.charAt(i);
            
            if(temp == '1'){    //모드 바꾸기 
                if(mode == 0){
                    mode = 1;
                    continue;
                }else {
                    mode = 0;
                    continue;
                }
            }
            // 모드가 0일 때    
            if(mode == 0 && i%2 == 0){
                ret += temp;
                
            }else if(mode == 1 && i%2 == 1) {
                ret += temp;
            }
            
        }    
    return ret.isEmpty() ? "EMPTY": ret;
    }
}