from collections import Counter

size = 4 

def view_matrix(matrix):   
    col_count = 0
    matr_2 =[]
    for i in range(size):
        matr_1 = []
        for j in range(size):
            if(col_count in matrix):
                matr_1.append(True)
            else:
               matr_1.append(False)
            col_count += 1
        matr_2.append(matr_1)
    return matr_2

def position(matrix):
    position_obj = []
    for i in range(size):
        for j in range(size):
            pos_obj = []
            if(matrix[i][j] == True):
                pos_obj.extend([i,j])
                position_obj.append(pos_obj)
    return position_obj

def neighbour_check(matrix,i):
    nb_true = []
    nb_false = []

    if (i[1]-1 >= 0 and i[0]-1 >= 0):
        if( matrix[i[0]-1][i[1]-1] == True):
             nb_true.append('t')
        elif (matrix[i[0]-1][i[1]-1] == False):
            pos_obj = []
            pos_obj.extend([i[0]-1,i[1]-1])
            nb_false.append(pos_obj)
        
    if (i[0]-1 >= 0):
        if(matrix[i[0]-1][i[1]] == True):
            nb_true.append('t')
        elif (matrix[i[0]-1][i[1]] == False):
            pos_obj=[]
            pos_obj.extend([i[0]-1, i[1]])
            nb_false.append(pos_obj)
                
    if (i[1]+1 < size and i[0]-1 >= 0):
        if(matrix[i[0]-1][i[1]+1] == True):
            nb_true.append('t')

        elif (matrix[i[0]-1][i[1]+1] == False):
            pos_obj = []
            pos_obj.extend([i[0]-1, i[1]+1])
            nb_false.append(pos_obj)

    if (i[1]-1 >= 0):
        if(matrix[i[0]][i[1]-1] == True):
            nb_true.append('t')
        elif (matrix[i[0]][i[1]-1] == False):
            pos_obj=[]
            pos_obj.extend([i[0], i[1]-1])
            nb_false.append(pos_obj)
        
    if (i[1]+1 < size):
        if(matrix[i[0]][i[1]+1] == True):
            nb_true.append('t')
        elif (matrix[i[0]][i[1]+1] == False):
            pos_obj=[]
            pos_obj.extend([i[0], i[1]+1])
            nb_false.append(pos_obj)
        
    if (i[1]-1 >= 0 and i[0]+1 < size):
        if(matrix[i[0]+1][i[1]-1] == True):
            nb_true.append('t')
        elif (matrix[i[0]+1][i[1]-1] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]-1])
            nb_false.append(pos_obj)

    if (i[0]+1 < size):
        if(matrix[i[0]+1][i[1]] == True):
            nb_true.append('t')
        elif (matrix[i[0]+1][i[1]] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]])
            nb_false.append(pos_obj)
               
    if (i[1]+1 < size and i[0]+1 < size):
        if(matrix[i[0]+1][i[1]+1] == True):
            nb_true.append('t')
        elif (matrix[i[0]+1][i[1]+1] == False):
            pos_obj=[]
            pos_obj.extend([i[0]+1, i[1]+1])
            nb_false.append(pos_obj)
    return len(nb_true),nb_false

def change_generation(matrix):
    new_matrix = matrix
    
    x = change_generation(matrix)  
    false = []
    dead = []
    
    for i in x:
        True_Cell, False_Cell = neighbour_check(matrix,i)
        if 2 < True_Cell < 3:
            dead.append(i)
        false.extend(False_Cell)

    for i in dead:
        matrix[i[0]][i[1]] = False
    count = Counter([tuple(i) for i in false])

    for key, values in count.items():
        if values == 3:
          matrix[key[0]][key[1]]=True

    return new_matrix