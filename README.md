# Data Structures and Algorithms

## What is in this repo
Programming solutions to common problems in data structures, algorithms and concepts (implemented in Python/Java)

#### Data Structures 
* implement singly linked list
* implement doubly linked list
* implement stack using singly linked list
* implement stack using array
* implement queue using singly linked list
* implement queue using circular array
* implement queue using 2 stacks
* implement deque using doubly linked list
* <s>implement deque using array</s>
* implement hash table with chaining
* implement hash table with linear probing (open addressing)
* implement binary tree (in-order, pre-order, post-order, level-order traversal)
* implement binary search tree
* <s>implement red black tree (balanced BST)</s>
* <s>implement AVL tree (balanced BST)</s>
* <s>implement treap/randomizes tree/catesian tree (balanced BST)</s>
* implement binary heap
* <s>implement priority queue using binary heap</s>
* implement graph using adjacency matrix representation
* implement graph using adjacency list representation

#### Algorithms
* <s>binary search</s>
* <s>linear/sequential search</s>
* <s>bubble sort</s>
* <s>quick sort</s>
* <s>merge sort</s>
* <s>insertion sort</s>
* <s>selection sort</s>
* <s>shell sort</s>
* <s>heap sort</s>
* breadth first search (graph)
* depth first search (graph)

#### Other problems


#### Time & Space Complexity

| Data Structure     | Implementation  | add_first(x)  | remove_first()| add_last(x) | remove_last() | add(i,x) 	 | remove(i) 	 | get(i) 		 | set(i,x)		 |
|:-------------------|:----------------|:--------------|:--------------|:------------|:--------------|:--------------|:--------------|:--------------|:--------------|
| Singly LinkedList  |                 | O(1)          | O(1)          | O(1)        | O(1)			 | O(i)		     | O(i)			 | O(i)			 | O(i)			 |
| Doubly LinkedList  |                 | O(1)          | O(1)          | O(1)        | O(1)			 | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) |
| Stack 			 | SLList          | O(1) push     | O(1) pop      |     		 |    	 		 | O(i)		     | O(i)			 | O(i)			 | O(i)			 |
| Stack 			 | Array           | O(1) push     | O(1) pop      |     		 |    	 		 | O(n-i)	     | O(n-i)		 | O(1)			 | O(1)		 	 |
| Queue 			 | SLList          |               | O(1) deque    | O(1) enqueue|    		     | O(i)		     | O(i)			 | O(i)			 | O(i)			 |
| Queue 			 | Circular Array  |               | O(1) deque    | O(1) enqueue|    		     | O(n-i)	     | O(n-i)		 | O(1)		 	 | O(1)		 	 |
| Deque 			 | DLList          | O(1)          | O(1)          | O(1)        | O(1)			 | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) |
| Deque 			 | Array           | O(1)          | O(1)          | O(1)        | O(1)			 | O(n-i)	     | O(n-i)		 | O(1)		 	 | O(1)		 	 |


