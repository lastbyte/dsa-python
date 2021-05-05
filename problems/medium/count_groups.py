

def mark_related(related, visited, i):
    n = len(related)
    for j in range(n):
        if visited[j] == 0 and related[i][j] == 1 :
            visited[j] = 1
            mark_related(related, visited, j)


def count_groups(related):
    n = len(related)

    if n == 0:
        return 0
    visited = [0] * n
    n_groups = 0

    for i in range(n):
        if visited[i] == 0 :
            mark_related(related, visited, i)
            n_groups +=1
    return n_groups

print(count_groups(related=[[1,1,0,0], [1,1,1,0], [0,1,1,0], [0,0,0,1]]))