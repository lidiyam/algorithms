# import Queue as Q

# q = Q.PriorityQueue()
# q.put((10, 'last'))
# q.put((1, 'first'))
# q.put((5, 'm'))
# while not q.empty():
# 	print q.get(),
class Node(object):
	def __init__(self, K, V):
		self.K = K
		self.V = V

class PriorityQ(object):
	heap = []
	d = {}

	def bubbleUp(cur):
		while cur > 0 and parent(cur).val < cur.val:
            swap(cur, parent(cur))
            cur = parent(cur)

    def update(old, new):
    	idx = d[old]
    	heap[idx] = new
    	bubbleUp(idx)

	def insert(el):
		heap.add(el)
		d[el] = len(heap)-1
		bubbleUp(len(heap)-1)


"""
class PriorityQueue<E extends Comparable<E>> {
    List<E> heap = new ArrayList<E>();
    Map<E, Integer> map = new HashMap<E, Integer>();

    void insert(E e) {
        heap.add(e);
        map.put(e, heap.size() - 1);
        bubbleUp(heap.size() - 1);
    }

    E deleteMax() {
        if(heap.size() == 0)
            return null;
        E result = heap.remove(0);
        map.remove(result);
        heapify(0);
        return result;
    }

    E getMin() {
        if(heap.size() == 0)
            return null;
        return heap.get(0);
    }

    void update(E oldObject, E newObject) {
        int index = map.get(oldObject);
        heap.set(index, newObject);
        bubbleUp(index);
    }

    private void bubbleUp(int cur) {
        while(cur > 0 && heap.get(parent(cur)).compareTo(heap.get(cur)) < 0) {
            swap(cur, parent(cur));
            cur = parent(cur);
        }
    }

    private void swap(int i, int j) {
        map.put(heap.get(i), map.get(heap.get(j)));
        map.put(heap.get(j), map.get(heap.get(i)));
        E temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    private void heapify(int index) {
        if(left(index) >= heap.size())
            return;
        int bigIndex = index;
        if(heap.get(bigIndex).compareTo(heap.get(left(index))) < 0)
            bigIndex = left(index);
        if(right(index) < heap.size() && heap.get(bigIndex).compareTo(heap.get(right(index))) < 0)
            bigIndex = right(index);
        if(bigIndex != index) {
            swap(bigIndex, index);
            heapify(bigIndex);
        }
    }

    private int parent(int i) {
        return (i - 1) / 2;
    }

    private int left(int i) {
        return 2*i + 1;
    }

    private int right(int i) {
        return 2*i + 2;
    }
}
"""

import heapq

heap = []
d = {'one': 0}
heapq.heappush(heap, (1, 'one'))
heapq.heappush(heap, (10, 'ten'))
heapq.heappush(heap, (5,'five'))
heapq.heappush(heap, (25,'tw five'))

while heap:
	print heapq.heappop(heap)
