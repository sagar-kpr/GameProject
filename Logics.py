import random as r
def start_game():
    mat=[[0 for i in range(4)] for j in range(4)]
    return mat
def add_nbr(mat):
    row = r.randint(0, 3)
    col = r.randint(0, 3)
    while mat[row][col] != 0:
        row = r.randint(0, 3)
        col = r.randint(0, 3)
    mat[row][col]=2
    return mat

def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0 :
                mat[i][j] = mat[i][j]*2
                mat[i][j+1]=0
                changed = True
    return mat, changed



def compress(mat):
    changed = False
    new_mat = [[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j] != 0 :
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos+=1
    return new_mat, changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

def move_left(mat):
    comp_mat, changed1 = compress(mat)
    merge_mat, changed2 = merge(comp_mat)
    changed = changed1 or changed2
    final_mat, temp = compress(merge_mat)

    return final_mat, changed

def move_right(mat):
    rev_mat = reverse(mat)
    comp_mat, changed1 = compress(rev_mat)
    merge_mat, changed2 = merge(comp_mat)
    changed = changed1 or changed2
    comp_mat_again, temp= compress(merge_mat)
    final_mat = reverse(comp_mat_again)

    return final_mat, changed

def move_up(mat):
    trans_mat = transpose(mat)
    comp_mat, changed1 = compress(trans_mat)
    merge_mat, changed2 = merge(comp_mat)
    changed = changed1 or changed2
    comp_mat_again, temp = compress(merge_mat)
    final_mat = transpose(comp_mat_again)

    return final_mat, changed

def move_down(mat):
    rev_mat = reverse(mat)
    trans_mat = transpose(rev_mat)
    comp_mat, changed1 = compress(trans_mat)
    merge_mat, changed2 = merge(comp_mat)
    changed = changed1 or changed2
    comp_mat_again, temp = compress(merge_mat)
    trans_mat_again = transpose(comp_mat_again)
    final_mat = reverse(trans_mat_again)

    return final_mat, changed

def status_of_game(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 8) :

                return 'WON'
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0) :
                return 'Game not over'
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1]) :
                return 'Game not over'
    for j in range(3) :
        if (mat[3][j] == mat[3][j+1]):
            return 'Game not over'

    for i in range(3):
        if (mat[i][3] == mat[i+1][3]):
            return 'Game not over'
    return 'LOST'


