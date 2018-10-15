#include<iostream>
#include<algorithm>
using namespace std;

#include<string.h>
#include<math.h> 

#define MAXN 300000
#define MAX (1+(1<<23))
#define inf 0x7fffffff

int arr[MAXN];
int tree[MAX];
int lazy[MAX];

/**
 * Build and init tree
 */
void build_tree(int node, int a, int b) {
  	if(a > b) return; // Out of range
  	
  	if(a == b) { // Leaf node
    		tree[node] = arr[a]; // Init value
		return;
	}
	
	build_tree(node*2, a, (a+b)/2); // Init left child
	build_tree(node*2+1, 1+(a+b)/2, b); // Init right child
	
	tree[node] = max(tree[node*2], tree[node*2+1]); // Init root value
}

/**
 * Increment elements within range [i, j] with value value
 */
void update_tree(int node, int a, int b, int i, int j, int value) {
  
  	if(lazy[node] != 0) { // This node needs to be updated
   		tree[node] += lazy[node]; // Update it

		if(a != b) {
			lazy[node*2] += lazy[node]; // Mark child as lazy
    			lazy[node*2+1] += lazy[node]; // Mark child as lazy
		}

   		lazy[node] = 0; // Reset it
  	}
  
	if(a > b || a > j || b < i) // Current segment is not within range [i, j]
		return;
    
  	if(a >= i && b <= j) { // Segment is fully within range
    		tree[node] += value;

		if(a != b) { // Not leaf node
			lazy[node*2] += value;
			lazy[node*2+1] += value;
		}

    		return;
	}

	update_tree(node*2, a, (a+b)/2, i, j, value); // Updating left child
	update_tree(1+node*2, 1+(a+b)/2, b, i, j, value); // Updating right child

	tree[node] = max(tree[node*2], tree[node*2+1]); // Updating root with max value
}

/**
 * Query tree to get max element value within range [i, j]
 */
int query_tree(int node, int a, int b, int i, int j) {
	
	if(a > b || a > j || b < i) return -inf; // Out of range

	if(lazy[node] != 0) { // This node needs to be updated
		tree[node] += lazy[node]; // Update it

		if(a != b) {
			lazy[node*2] += lazy[node]; // Mark child as lazy
			lazy[node*2+1] += lazy[node]; // Mark child as lazy
		}

		lazy[node] = 0; // Reset it
	}

	if(a >= i && b <= j) // Current segment is totally within range [i, j]
		return tree[node];

	int q1 = query_tree(node*2, a, (a+b)/2, i, j); // Query left child
	int q2 = query_tree(1+node*2, 1+(a+b)/2, b, i, j); // Query right child

	int res = max(q1, q2); // Return final result
	
	return res;
}

int find_loc(int NODE_LOC, int left, int right){
	
	if(left == right || right < left){
		return NODE_LOC;
	}
	
	int left_val = query_tree(1, 0, MAXN-1, left, (left + right) / 2);
	int right_val = query_tree(1, 0, MAXN-1, (left + right)/2 , right);
	
	if(left_val >= right_val){
		return find_loc(NODE_LOC, left, (left + right) / 2);	
	}else{
		return find_loc(NODE_LOC + 1 +  (left+right)/2, (left+right)/2 + 1, right);
	}
}


int main() {
	for(int i = 0; i < MAXN; i++) arr[i] = 0;
	build_tree(1, 0, MAXN-1);
	memset(lazy, 0, sizeof lazy);
	
	int N, M;
	cin >> N >> M;
	int locs[M];
	for (int i =0;i<M;i++){
		cin >> locs[i];
	}
	for(int i =0;i<M-1;i++){
		int a = locs[i];
		int b = locs[i+1];
		if(b < a){
			int tmp = b;
			b = a;
			a = tmp;
		}
		//cout << "updaing" << a << "|" << b << endl;
		update_tree(1, 0, MAXN-1, a, b, 1);
	}
	int answer = query_tree(1, 0, MAXN-1, 0, MAXN-1); // << endl;
	cout << find_loc(0, 0, N-1) << endl;
	
}