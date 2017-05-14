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

    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int[] otherNums = {3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6};
        int maxSubArr = maxSubArrayBetter(nums);

        System.out.println("max: " + maxSubArr);
        System.out.println(containsDuplicate(nums));
        System.out.println(reverseString("hello"));
        List<Integer> top = topKFrequent(otherNums,10);
    }
}