import java.lang.*; 

class Solution {
    public String solution(String s) {
        s=s.toLowerCase();
        String[] st = s.split("");
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        
        for(int i = 0; i < st.length; i++) {
            
            if(st[i].equals(" ")) {
                flag = true;
                sb.append(st[i]);
            }else{
                if(flag == true){
                    st[i] = st[i].toUpperCase();
                    flag = false;
                }
                sb.append(st[i]);
            }   
        }

        return sb.toString();
        
    }
}