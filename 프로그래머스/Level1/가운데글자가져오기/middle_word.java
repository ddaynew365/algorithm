class Solution {
    public String solution(String s) {
        String answer = "";
        int len_s = s.length();
        int locate = len_s/2;
        if (len_s % 2 ==0){
            answer += s.substring(locate-1,locate+1);
        }
        else{
            answer += s.substring(locate,locate + 1);
        }
        return answer;
    }
}
