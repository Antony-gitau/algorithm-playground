#include <iostream>
#include <vector>
using namespace std;

int main(){
// bfs algorithm
int bfs (int startNode){ // the root node is the variable of this function
 queue<int> bfsQueue; //create a queue that will contain integer data type
 vector<bool> visited(n) ; //make the node as visited or not visited.
 int visCount = 0; //start counting the visited nodes from 0


visited[startNode] = true; //mark the root node as visited
bfsQueue.push(startNode); //push the node to the queue

while (!bfsQueue.empty()) //as long as the queue is  not empty
{     
    int currentNode = bfsQueue.front(); //go to the next node - which is the front one in the queue
    bfsQueue.pop(); //pop it from the queue

     for( auto neighbours: graph[currentNode]){ //visit one of its neigbour
        if( !visited[neighbour]){ //if the neighbour is not visited, 
            visited[neighbour] == true; //label them visited,
            bfsQueue.push(neighbour); //and push them to the queue
        }
     }
     visCount +=1;
}
return visCount;
}
}