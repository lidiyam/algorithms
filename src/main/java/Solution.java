import java.util.*;

public class Solution {
    public static int maxSubArray(int[] nums) {
        List<Integer> maxSumsGlobal = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) {
            int localMax = 0;
            List<Integer> maxSums = new ArrayList<Integer>();
            for (int j = i; j < nums.length; j++) {
                localMax += nums[j];
                maxSums.add(localMax);
            }
            maxSumsGlobal.add(Collections.max(maxSums));
        }
        return Collections.max(maxSumsGlobal);
    }

    public static int maxSubArrayBetter(int[] A) {
        int maxSubArr = A[0];
        int maxEndingHere = A[0];
        for (int i = 1; i < A.length; ++i) {
            maxEndingHere = Math.max(maxEndingHere + A[i], A[i]);
            maxSubArr = Math.max(maxSubArr, maxEndingHere);
        }
        return maxSubArr;
    }

    public static boolean containsDuplicate(int[] nums) {
        if (nums == null || nums.length <=1) return false;
        final Set<Integer> lst = new HashSet<Integer>();
        for (int num : nums) {
            if (lst.contains(num)) return true;
            lst.add(num);
        }
        return false;
    }

    public static String reverseString(String s) {
        int len = s.toCharArray().length;
        char[] str = new char[len];
        for (int i = 0; i < len; i++) {
            str[len-1 - i] = s.charAt(i);
        }
        return new String(str);
    }

    public static List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num,map.get(num)+1);
            } else {
                map.put(num,1);
            }
        }
        List<Integer> topK = new ArrayList<Integer>();
        List<Integer> topC = new ArrayList<Integer>();
        for (int i = 0; i < k; i++) {
            topC.add(i,0);
            topK.add(i,0);
        }
        for (int key : map.keySet()) {
            for (int i = 0; i < k; i++) {
                if (map.get(key) > topC.get(i)) {
                    topC.set(i, map.get(key));
                    topK.set(i, key);
                    break;
                }
            }
        }
        return topK;
    }

    public static int bstHeight(int[] a, int i) {
        if (a[i+1] == -1 && a[i+2] == -1) return 1;
        else {
            return 1 + Math.max(bstHeight(a, a[i+1]), bstHeight(a,a[i+2]));
        }
    }

    static int[] A = {4,2,3,0,1};
    static int n = 5;

    public static void loop1(int i) {
        int index = A[i];
        int temp = A[index];
        A[index] = index;
        A[i] = temp;
        if (i == temp && i == (n-1)) { //done
            return;
        } else if (i == temp) {
            A[i] = temp;
            ++i;
        }
        loop1(i);
    }

    public static void printArr() {
        for (int i=0; i < n; ++i) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int[] otherNums = {3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6};
        int maxSubArr = maxSubArrayBetter(nums);

        System.out.println("max: " + maxSubArr);
        System.out.println(containsDuplicate(nums));
        System.out.println(reverseString("hello"));
        List<Integer> top = topKFrequent(otherNums,10);

        int[] bst = {77,3,6,22,-1,-1,-8,9,12,-36,-1,-1,999,-1,-1};
        int[] bst = {77,-1,-1};
        System.out.println(bstHeight(bst, 0));
        printArr();
        loop1(0);
        printArr();
    }
}