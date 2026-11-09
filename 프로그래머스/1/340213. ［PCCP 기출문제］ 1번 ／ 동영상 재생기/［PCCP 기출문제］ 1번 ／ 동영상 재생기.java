import java.util.*;
class Solution {
    
    public boolean isOpenning(int c_time, int s, int e) {
        if (s <= c_time && c_time <= e) {
            return true;
        }
        return false;
    }
    
    public int stringToTime(String time) {
        int temp = 0;
        temp += (time.charAt(0)-'0')*600;
        temp += (time.charAt(1)-'0')*60;
        temp += (time.charAt(3)-'0')*10;
        temp += (time.charAt(4)-'0');
        return temp;
    }
    
    public String timeToString(int time) {
        StringBuilder sb = new StringBuilder();
        int min = time / 60;
        int sec = time % 60;
        
        if (min < 10){
            sb.append("0");
        }
        sb.append(min);
        sb.append(":");
        if (sec < 10) {
            sb.append("0");
        }
        sb.append(sec);
        
        return sb.toString();
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        // Pos를 변경해서 처리
        int c_time = stringToTime(pos);
        int s = stringToTime(op_start);
        int e = stringToTime(op_end);
        
        // 포함x
        int max_time= stringToTime(video_len);
        // 포함x
        int min_time= 0;
        // 이후 명령어 수행
        for(String cmd : commands){
            // 시작할때 오프닝 이면 끝냄
            if (isOpenning(c_time, s, e)){
                c_time = e;
            }

            if (cmd.equals("next")){
                if (c_time + 10 >= max_time) {
                    c_time = max_time;
                    continue;
                }
                c_time+=10;
            }
            else if (cmd.equals("prev")){
                if (c_time - 10 <= min_time) {
                    c_time = min_time;
                    continue;
                }
                c_time-=10;
            }
        }
        if (isOpenning(c_time, s, e)){
                c_time = e;
        }
        
        String answer = timeToString(c_time);
        return answer;
    }
}