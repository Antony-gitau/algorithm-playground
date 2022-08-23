
Graphs in computer science are used to show relationships (edges /lines of connection) between objects (nodes/vertices).

Graphs can be directed or undirected. Here are real life application examples of the two types of graphs in use:

1. Facebook uses undirected graphs to map the friendship connections on their platform. This means that for two people (nodes) - say A and B with friendship connection (edge). A is much a friend to B as B is to A.

2. This is different for Twitter. In the "followship" algorithm unlike "friendship" algorithm in Facebook, Twitter assumes that person A can follow person B yet person B does not have to follow person A. This means that it matters who follows who - simply put the "direction of followship". This in practise is directed graph. 


---
Breadth first search (BFS) algorithm
---

BFS is used to determine whether an undirected graph is connected or not. This is literally travesing through all nodes in the graph - if all of them can be accessed, then thats a connected graph, else it is disconnected.

pseudocode:
1. visit a random node (root node).
2. visit all the neighbours (nodes) of the root node and push them to a queue.
3. pop the first node in the queue >> visit all its neighbours (nodes) >> push only the neighbours who haven't been earlier visited to the queue.
4. repeat step three as long as the queue is not empty.
5. once the queue is empty, then all the reachable nodes have been visited.

resources:
1. I found [csacademy](https://csacademy.com/lesson/breadth_first_search) very useful.