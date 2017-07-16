
public class RabinKarpAlgorithm {
    private int prime = 97;

    public int patternSearch(char[] text, char[] pattern) {
        int m = pattern.length;
        int n = text.length;
        long patternHash = toHash(pattern, m - 1);
        long textHash = toHash(text, m - 1);
        for (int i = 1; i <= n - m + 1; i++) {
            if (patternHash == textHash && checkEqual(text, i - 1, i + m - 2, pattern, 0, m - 1)) {
                return i - 1;
            }
            if (i < n - m + 1) {
                textHash = nextHash(text, i - 1, i + m - 1, textHash, m);
            }
        }
        return -1;
    }

    private long nextHash(char[] str, int prevIndex, int nextIndex, long prevHash, int patternLen) {
        long nextHash = prevHash - str[prevIndex];
        nextHash = nextHash/prime;
        nextHash += str[nextIndex]*Math.pow(prime, patternLen - 1);
        return nextHash;
    }

    private long toHash(char[] str, int end){
        long hash = 0;
        for (int i = 0 ; i <= end; i++) {
            hash += str[i] * Math.pow(prime,i);
        }
        return hash;
    }

    private boolean checkEqual(char str1[], int start1, int end1, char str2[], int start2, int end2){
        if (end1 - start1 != end2 - start2) {
            return false;
        }
        while (start1 <= end1 && start2 <= end2) {
            if (str1[start1] != str2[start2]) {
                return false;
            }
            start1++;
            start2++;
        }
        return true;
    }

    public static void main(String args[]){
        RabinKarpAlgorithm rk = new RabinKarpAlgorithm();
        System.out.println(rk.patternSearch("abedceabc".toCharArray(), "abc".toCharArray()));
        System.out.println(rk.patternSearch("This is a simple example".toCharArray(), "example".toCharArray()));
    }
}
