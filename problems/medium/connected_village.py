'''
          |1 1 1 0 0 0|
          |0 1 1 0 0 0|
 village 1|0 1 0 0 0 0| village 2
          |0 1 0 0 0 0|
          |1 1 1 0 0 0|
          |1 0 1 1 1 1|

 two villages are seperated by a river stream represented as an array of 0's and 1's ,
 1 represents rock and 0 represents water. a person can only walk on the rock , find if
 there is any possible way to reach from village 1 to village 2.

'''



def is_connected(arr, width, height):
    visited = [[False]*width for i in range(height)]
    for i in range(height):
        queue = []
        if not visited[i][0] and arr[i][0] == 1:
            queue.append([i, 0])
        while len(queue) > 0:
            [i, j] = queue.pop(0)
            visited[i][j] = True

            if j == (width - 1):
                return True

            if (j - 1) >= 0 and arr[i][j - 1] == 1 and visited[i][j - 1] == False:
                queue.append([i, j - 1])
            if (j + 1) < width and arr[i][j + 1] == 1 and visited[i][j + 1] == False:
                queue.append([i, j + 1])
            if (i - 1) >= 0 and arr[i - 1][j] == 1 and visited[i - 1][j] == False:
                queue.append([i - 1, j])
            if (i + 1) < height and arr[i + 1][j] == 1 and visited[i + 1][j] == False:
                queue.append([i + 1, j])

    return False


print(is_connected([[1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1]], 6, 6))
