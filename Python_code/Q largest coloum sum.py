def lar_Col_Sum(li):
    n = len(li)
    m = len(li[0])
    max_sum = -1
    max_col_Index = -1
    for j in range(m):  # going through each column
        sum = 0
        for i in range(n):  # gowing throw each row
            sum += li[i][j]
        if sum > max_sum:
            max_col_index = j
            max_sum = sum
    return max_sum, max_col_index


li = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12]]
lar_sum, lar_col_index = lar_Col_Sum(li)
print(lar_sum, lar_col_index)


def lar_Col_Sum(li):
    n = len(li)
    m = len(li[0])
    max_sum = -1
    max_col_Index = -1
    for j in range(m):  # going through each column
        sum = 0
        for ele in li:
            sum += ele[j]
        if sum > max_sum:
            max_col_index = j
            max_sum = sum
    return max_sum, max_col_index


li = [[1, 2, 3, 4], [8, 7, 6, 5], [9, 10, 11, 12]]
lar_sum, lar_col_index = lar_Col_Sum(li)
print(lar_sum, lar_col_index  )