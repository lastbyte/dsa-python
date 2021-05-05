'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
'''


class Solution:
    def connected_components(self, n, edges):
        adjacency_matrix = self.create_2d_matrix(n, n, False)

        for edge in edges:
            adjacency_matrix[edge[0]][edge[1]], adjacency_matrix[edge[1]][
                edge[0]] = True, True
        return self.connected_components_util(n, adjacency_matrix)

    def connected_components_util(self, n, adjacency_matrix):

        if n == 0 or n == 1:
            return n

        visited = [False] * n
        connected_nodes = 0
        for index in range(n):
            if not visited[index]:
                self.mark_connected(n, adjacency_matrix, visited, index)
                connected_nodes += 1

        return connected_nodes

    def mark_connected(self, n, adjecnecy_matrix, visited, current_index):

        for new_index in range(n):
            if not visited[new_index] and adjecnecy_matrix[current_index][
                    new_index]:
                visited[new_index] = True
                self.mark_connected(n, adjecnecy_matrix, visited, new_index)

    def create_2d_matrix(self, rows, cols, default):
        return [[default] * cols for row in range(rows)]


result = Solution().connected_components(5, [[0, 1], [1, 2], [3, 4]])
print(result)

result = Solution().connected_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
print(result)

result = Solution().connected_components(2, [[1, 0]])
print(result)
