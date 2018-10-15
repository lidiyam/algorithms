#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm> 
#include <utility>

using namespace std;

struct KDNode {
	int x, y;
	KDNode *left;
	KDNode *right;

	KDNode(int x, int y): x{x}, y{y}, left{nullptr}, right{nullptr} {}
	KDNode(pair<int,int> tuple): x{tuple.first}, y{tuple.second}, left{nullptr}, right{nullptr} {}
	~KDNode() {
		delete left;
		delete right;
	}
};

struct KDTree {
	KDNode *root;
	~KDTree() {
		delete root;
	}
};

// comparisons
bool byX(pair<int,int> p1, pair<int,int> p2) {
	return (p1.first < p2.first);
}

bool byY(pair<int,int> p1, pair<int,int> p2) {
	return (p1.second < p2.second);
}


// construct a kd-tree for dimension 2
KDNode* buildKDTree(vector<pair<int,int>> points, bool splitX = true) {
	if (points.size() == 0) return nullptr;
	int median = points.size() / 2;
	if (splitX) {
		nth_element(points.begin(), points.begin()+median, points.end(), byX);
	} else {
		nth_element(points.begin(), points.begin()+median, points.end(), byY);
	}

	KDNode *root = new KDNode(points[median]);

	vector<pair<int,int>> leftPoints(points.begin(), points.begin() + median);
	vector<pair<int,int>> rightPoints(points.begin() + median+1, points.end());
	root->left = buildKDTree(leftPoints,!splitX);
	root->right = buildKDTree(rightPoints,!splitX);
	return root;
}


void preOrder(KDNode *n, ostringstream &out) {
	if (n == nullptr) return;
	out << n->x << " " << n->y << " ";
	preOrder(n->left,out);
	preOrder(n->right,out);
}


int main() {
	// read in 2n + 1 ints
	int n;
	cin >> n;

	int x, y;
	vector< pair<int,int> > points;
	for (int i = 0; i < n; ++i) {
		cin >> x;
		cin >> y;
		points.push_back(make_pair(x,y));
	}

	KDTree *t = new KDTree();
	t->root = buildKDTree(points,true);

	// output pre-order traversal of KDTree
	ostringstream ss;
	preOrder(t->root,ss);
	string s = ss.str();

	if (s.length() > 0) {
		cout << s.substr(0,s.length()-1) << endl;
	}

	delete t;

}