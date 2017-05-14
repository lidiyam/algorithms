/**
 * Heaps
 */
public class PriorityQueue {

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
    public static void deleteMax(int[] A, int heapSize) {
        int temp = A[0];
        A[0] = A[heapSize-1];
        A[heapSize-1] = temp;

        heapSize -= 1;
        Heaps.maxHeapify(A,0,heapSize);
    }
}
