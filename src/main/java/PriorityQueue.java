/**
 * Heaps
 */
public class PriorityQueue {

    public static int heapMax(int[] A) {
        return A[0];
    }

    // Place new element at the first free leaf, bubble-up
    // O(log(n))
    public static void insert(int[] A, int v, int heapSize) {
        heapSize += 1;
        A[heapSize-1] = v;
        int i = heapSize-1;
        int parent = (i-1)/2;

        while (parent >= 0 && A[parent] < A[i]) {
            // swap v and parent
            int temp = A[i];
            A[i] = A[parent];
            A[parent] = temp;
            i = parent;
            parent = (i-1)/2;
        }
    }

    // O(log(n))
    public static int deleteMax(int[] A, int heapSize) {
        if (heapSize < 1) return -1;
        int max = A[0];
        A[0] = A[heapSize-1];
        A[heapSize-1] = max;
        heapSize -= 1;
        Heaps.maxHeapify(A,0,heapSize);
        return max;
    }

    // O(log(n))
    public static void deleteMin(int[] A, int heapSize) {
        int temp = A[0];
        A[0] = A[heapSize-1];
        A[heapSize-1] = temp;
        heapSize -= 1;
        Heaps.minHeapify(A,0,heapSize);
    }

    // Increase value of element A[i] to key in a max-heap A
    // O(log(n))
    public static void increaseKey(int[] A, int i, int key, int heapSize) {
        if (A[i] > key) return;
        A[i] = key;
        int parent = (i-1)/2;

        while (parent >= 0 && A[parent] < A[i]) {
            // swap
            int temp = A[i];
            A[i] = A[parent];
            A[parent] = temp;
            i = parent;
            parent = (i-1)/2;
        }
    }
}
