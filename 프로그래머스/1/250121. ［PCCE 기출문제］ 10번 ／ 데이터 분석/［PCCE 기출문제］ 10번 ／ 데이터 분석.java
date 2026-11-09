import java.util.*;
class Solution {
    
    static List<Data> da;
    
    public class Data implements Comparable<Data> {
        int code;
        int date;
        int maximum;
        int remain;
        int sortType;
        
        public Data(int[] d, int sortType) {
            this.code = d[0];
            this.date = d[1];
            this.maximum = d[2];
            this.remain = d[3];
            this.sortType = sortType;
        }
        
        @Override
        public int compareTo(Data o) {
            
            if (sortType == 0) {
                return Integer.compare(this.code, o.code);
            }
            else if (sortType == 1) {
                return Integer.compare(this.date, o.date);
            }
            else if (sortType == 2) {
                return Integer.compare(this.maximum, o.maximum);
            }
            else if (sortType == 3) {
                return Integer.compare(this.remain, o.remain);
            }
            
            return 0;
        }
    }
    
    public static int changeExt(String ext) {
        System.out.println(ext);
        if (ext.equals("code")) {
            return 0;
        }
        else if (ext.equals("date")) {
            return 1;
        }
        else if (ext.equals("maximum")) {
            return 2;
        }
        else if (ext.equals("remain")) {
            return 3;            
        }
        return -1;
    }
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        da = new ArrayList<Data>();
        int cmp_value = changeExt(ext);
        int sortType = changeExt(sort_by);
        for(int[] d : data) {
            // 작지 않은 경우 처리 x
            if (!(val_ext > d[cmp_value])){
                continue;
            }
            da.add(new Data(d, sortType));
        }
        
        Collections.sort(da);
        int[][] answer = new int[da.size()][4];
        for(int i = 0; i < da.size(); i++){
            answer[i][0] = da.get(i).code;
            answer[i][1] = da.get(i).date;
            answer[i][2] = da.get(i).maximum;
            answer[i][3] = da.get(i).remain;
        }
        
        return answer;
    }
}