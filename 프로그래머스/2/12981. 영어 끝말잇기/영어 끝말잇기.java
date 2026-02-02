class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int[] count = new int[n];
        boolean isEnd = false;
        for(int i = 1; i < words.length; i++) {
            int number = i%n+1;
            String word = words[i];
            String preWord = words[i-1];
            
            // 이전에 있었는가?
            for (int j=0; j < i; j++) {
                if (words[j].equals(word)) {
                    System.out.printf("word : %s\n", word);
                    answer[0] = number;
                    answer[1] = (i/n)+1;
                    isEnd = true;
                    break;
                }
            }
            if (isEnd) {
                break;
            }
            
            // 끝말 규칙
            if (word.charAt(0) != preWord.charAt(preWord.length()-1)) {
                answer[0] = number;
                answer[1] = (i/n)+1;
                System.out.printf("word : %s, preWord: %s\n", word, preWord);
                break;
            }
        }
        
        return answer;
    }
}