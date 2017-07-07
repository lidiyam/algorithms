import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Stack;

public class Leetcode {

    public static boolean slice(String s, String[] words, int wordLen) {
        int [] marked = new int[wordLen+1];
        int i = 0;
        while (i+wordLen <= s.length()) {
            String sub = s.substring(i, i+wordLen);
            int found = contains(words,sub);
            if (found == -1) return false;
            if (marked[found] == 1) return false;
            marked[found] = 1;
            i += wordLen;
        }
        return true;
    }

    public static int contains(String[] words, String s) {
        for (int i=0; i<words.length;i++) {
            if (words[i].equals(s)) return i;
        }
        return -1;
    }

    public static List<Integer> findSubstring(String s, String[] words) {
        List<Integer> list = new LinkedList<Integer>();
        int totalWords = words.length;
        if (totalWords == 0) return list;
        int wordLen = words[0].length(); // words are all the same length
        int totalSubLen = wordLen*totalWords;

        int i = 0;
        while (i + totalSubLen <= s.length()) {
            String sub = s.substring(i, i+totalSubLen);
            if (slice(sub,words,wordLen)) {
                list.add(i);
                i += wordLen;
            } else {
                i += 1;
            }
        }
        return list;
    }

    public static int reverse(int x) {
        int c = x;
        if (Integer.MAX_VALUE / 10 < res || (Integer.MAX_VALUE - x % 10) < res * 10) {
            return 0;
        }
        Queue<Integer> lst = new LinkedList<Integer>();
        while (c != 0) {
            int r = c % 10;
            c = c / 10;
            lst.add(r);
        }
        c = 0;
        int t = (int) Math.pow(10,lst.size()-1);
        while (!lst.isEmpty()) {
            c = c + lst.remove()*t;
            t = t / 10;
        }
        return c;
    }

    public static void main(String[] args) {
        String[] words = {"bar","foo","the"};
        String[] words2 = {"bar","foo"};

        String s1 = "barfoofoobarthefoobarman";
        String s2 = "barfoothefoobarman";

        String s3 = "abababab";
        String[] words3 = {"a","b"};

        String s4 = "aaabbbc";
        String[] words4 = {"a","a","b","b","c"};

        System.out.println(reverse(45));
        System.out.println(reverse(-45));
        System.out.println(reverse(1));
    }

}
