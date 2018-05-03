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
* binary search
* linear/sequential search
* bubble sort
* selection sort
* insertion sort
* quick sort
* merge sort
* heap sort
* breadth first search (graph)
* depth first search (graph)

#### Other problems


## Time & Space Complexity
* [Reference](http://bigocheatsheet.com/)

#### List & Array (Time complexity)

| Data Structure     | Implementation  | add_first(x)  | remove_first()| add_last(x)   | remove_last() | add(i,x) 	 	    | remove(i) 	 | get(i) 		 | set(i,x)		 |
|:-------------------|:----------------|:--------------|:--------------|:--------------|:--------------|:-------------------|:--------------|:--------------|:--------------|
| Singly LinkedList  |                 | O(1)          | O(1)          | O(1)          | O(1)		   | O(i)		        | O(i)			 | O(i)			 | O(i)			 |
| Doubly LinkedList  |                 | O(1)          | O(1)          | O(1)          | O(1)		   | O(min{i,n-i}) 	    | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) |
| Stack 			 | SLList          | O(1) push     | O(1) pop      |     		   |    	 	   | O(i)		        | O(i)			 | O(i)			 | O(i)			 |
| Stack 			 | Array           | O(1) push     | O(1) pop      |     		   |    	 	   | O(n-i)	            | O(n-i)		 | O(1)			 | O(1)		 	 |
| Queue 			 | SLList          |               | O(1) deque    | O(1) enqueue  |    		   | O(i)		        | O(i)			 | O(i)			 | O(i)			 |
| Queue 			 | Circular Array  |               | O(1) deque    | O(1) enqueue  |    		   | O(n-i)	            | O(n-i)		 | O(1)		 	 | O(1)		 	 |
| Deque 			 | DLList          | O(1)          | O(1)          | O(1)          | O(1)	 	   | O(min{i,n-i})      | O(min{i,n-i}) | O(min{i,n-i}) | O(min{i,n-i}) |
| Deque 			 | Array           | O(1)          | O(1)          | O(1)          | O(1)		   | O(n-i)	            | O(n-i)		 | O(1)		 	 | O(1)		 	 |

#### Tree (Time complexity)

| Data Structure     | search   | insert   | remove   | extractmin |
|:-------------------|:---------|:---------|:---------|:-----------|
| Binary Tree		 | O(n)     | O(n)     | O(n)     |            |  
| Binary Search Tree | avg O(h) = O(logn)|same|same|		       |
|					 | worst O(h)=O(n) for skewed tree|same|same|  |
| Binary Heap 		 | O(n)     | O(logn)  |          | O(1)       |

#### Graph (Time complexity)

| Representation    | BFS   		| DFS   		| add_edge(i,j)| remove_edge(i,j), has_edge(i,j) | out_edge(i), out_degree(i)| in_edge(u),in_degree(u)|			
|:------------------|:--------------|:--------------|:-------------|:--------------------------------|:--------------------------|:-----------------------|
| Adjacency Matrix  | `O(|V|+|E|)`  | `O(|V|+|E|)`  | O(1)         | O(1)                            | `O(|V|)`                  | `O(|V|)`               |
| Adjacency List    | `O(|V|+|E|)`  | `O(|V|+|E|)`  | O(1)         | O(deg(i))                       | O(1)                      | `O(|V|+|E|)`           |


#### Searching and Sorting Algorithms for Arrays (Time and Space complexity)

|					|Worst   |	Avg 	 |	Best 	 |Space   |
|:------------------|:-------|:----------|:----------|:-------|
|Bubble Sort 		|O(n^2)	 |	O(n^2)	 |	O(n)	 |	O(1)  |    
|Insertion Sort		|O(n^2)	 |	O(n^2)	 |	O(n)	 |	O(1)  |
|Selection Sort		|O(n^2)	 |	O(n^2)	 |	O(n^2)	 |	O(1)  |
|Merge Sort 	    |O(nlogn)|	O(nlogn) |	O(nlogn) |	O(n)  |
|Quick Sort 		|O(n^2)	 |	O(nlogn) |	O(nlogn) |	O(logn)|
|Heap Sort 			|O(nlogn)|	O(nlogn) |	O(nlogn) |	O(1)  |



