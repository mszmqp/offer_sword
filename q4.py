# 二维有序数组中查找相关的数

sign = 0

def find(a, v, i, j):

    global sign
    if sign == 1:
        return 0
    if i > 3 or j > 3:
        return 0

    print(i, j)
    print(a[i][j])

    if a[i][j] == v:
        sign = 1
    elif a[i][j] < v:
        newi = i+1
        find(a, v, newi, j)
        newj = j+1
        find(a, v, i, newj)
    elif a[i][j] > v:
        return 0


if __name__ == '__main__':

    a = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
    v = 7
    find(a, v, 0, 0)


