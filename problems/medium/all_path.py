'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

xample 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.

link -> https://leetcode.com/problems/all-paths-from-source-to-target/
'''

def all_path(graph):
    return all_path_util(graph, 0, len(graph)-1, [0], [])

def all_path_util(graph,current_node, target_node, current_path, all_paths):
    if current_node == target_node:
        all_paths.append(current_path.copy())
        current_path = []
    else :
        for i in graph[current_node]:
            all_path_util(graph, i, target_node, current_path + [i], all_paths)
    return all_paths




if __name__ == "__main__" :
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    result = all_path(graph)
    print(result)

    graph = [[1], []]
    result = all_path(graph)
    print(result)