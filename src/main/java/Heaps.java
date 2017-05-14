/**
 * Heaps
 */
public class Heaps {

    // Correct a single violation of the heap property in a subtree at its root
    // O(log(n))
    public static void maxHeapify(int[] A, int i, int heapSize) {     // bubble-down
        // Assume that the trees rooted at left(i) and right(i) are max-heaps
        int l = 2*i;
        int r = 2*i+1;
        int largest = i;

        if (l < heapSize && A[l] > A[i]) {
            largest = l;
        }
        if (r < heapSize && A[r] > A[largest]) {
            largest = r;
        }
        if (largest != i) {
            // swap
            int temp = A[i];
            A[i] = A[largest];
            A[largest] = temp;
            maxHeapify(A, largest, heapSize);
        }
    }


    // Produce max-heap from an unordered array A
    // O(n)
    public static void buildMaxHeap(int[] A) {
        // elements A[n/2 + 1 … n] are leaves of the tree
        for (int i = A.length/2; i >= 0; i--) {
            maxHeapify(A, i, A.length);
        }

    }

    // O(n*log(n))
    public static void heapsort(int[] A, int heapSize) {
        // Build Max Heap from unordered array
        buildMaxHeap(A);
        // Swap elements A[n] and max element at A[0], maxHeapify
        while (heapSize > 0) {
            int temp = A[0];
            A[0] = A[heapSize - 1];
            A[heapSize - 1] = temp;
            // Discard node n from heap
            heapSize = heapSize - 1;
            // maxHeapify new subtree
            maxHeapify(A, 0, heapSize);
        }
    }


    public static void main(String[] args) {
        int[] A = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
        printArray(A);
        heapsort(A, A.length);
        printArray(A);
        int[] B = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1, 0};
        PriorityQueue.insert(B,20,B.length-1);
        printArray(B);
        int[] C = {16, 14, 10, 8, 7, 9, 3, 2, 4, 1};
        PriorityQueue.deleteMax(C, C.length);
        printArray(C);
    }

    public static void printArray(int[] A) {
        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println();
    }
}
