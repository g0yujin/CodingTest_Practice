class Solution {
    public int solution(String number) {
        int total = 0;
        for(int i=0; i<number.length(); i++){
            int temp = number.charAt(i) - '0';
            total += temp;
        }
        return total%9;
    }
}