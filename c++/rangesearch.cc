#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm> 
#include <utility>

using namespace std;

struct Node {
	int data;
	Node *left;
	Node *right;

	Node(int x): data{x}, left{nullptr}, right{nullptr} {}
	~Node() {
		delete left;
		delete right;
	}

	void insert(int x) {
		if (this->data >= x)
	}
};

struct Tree {
	Node *head;
	Tree() {}
	~Tree() { delete head; }

	void insert(int x) {
		if (head == nullptr) head = new Node(x);
		else if (this->head->data >= x) {
			(this->head->left)->insert(x);
		} else {
			(this->head->right)->insert(x);
		}
	}
};

void inOrder(Node *n) {
	if (n == nullptr) return;
	inOrder(n->left);
	cout << n->data << " ";
	inOrder(n->right);
}

int main() {
	Tree *n = new Tree();
	n->insert(52);
	n->insert(35);
	n->insert(15);
	n->insert(27);
	n->insert(9);
	n->insert(42);
	n->insert(39);
	n->insert(46);
	n->insert(74);
	n->insert(65);

	inOrder(n->head);

	delete n;
}