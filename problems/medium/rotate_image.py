'''
rotate an image by 90 degree in clockwise direction
'''
def rotate_image(matrix):
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp

    print(matrix)


rotate_image([[1,2,3],[4,5,6],[7,8,9]])
rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])