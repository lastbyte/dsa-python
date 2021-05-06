def spiral_order(matrix):
    spiral = []
    return spiral_matrix(matrix, 0, len(matrix),0, len(matrix[0]), spiral)

def spiral_matrix(matrix, i_min, i_max, j_min, j_max, spiral):
    i = i_min
    j = j_min

    if (i_max-i_min == 1):
        while j < j_max:
            spiral.append(matrix[i][j])
            j += 1
        return spiral

    if (j_max - j_min == 1):
        while i < i_max:
            spiral.append(matrix[i][j])
            i += 1
        return spiral

    if i_min < i_max and j_min < j_max:
        while j < j_max:
            spiral.append(matrix[i][j])
            j += 1
        j -= 1
        i += 1
        while i < i_max:
            spiral.append(matrix[i][j])
            i += 1
        i -= 1
        j -= 1
        while j >= j_min:
            spiral.append(matrix[i][j])
            j -= 1
        j += 1
        i -= 1
        while i > i_min:
            spiral.append(matrix[i][j])
            i -= 1
        spiral_matrix(matrix, i_min + 1, i_max - 1, j_min + 1, j_max - 1, spiral)
    return spiral




print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(spiral_order([[1]]))
print(spiral_order([[7], [9], [6]]))
 