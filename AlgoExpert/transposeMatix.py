
def Solution1(matrix):

    TransposedMatric = []
    for col in range(len(matrix[0])):
        ModRow = []
        for row in range(len(matrix)):
            ModRow.append(matrix[row][col])
        TransposedMatric.append(ModRow)
    return TransposedMatric


def Solution2(matrix):
    return print(list(zip(*matrix)))

# *matrix unpack the matrix into list of rows 
# zipping them means take "i"th element of each list to make a tuple


# --------------------------------------------------------------------------------------------------------------------------

# matrix = [[4,2,5],[-1,5,0],[0,-4,6]]

# matrix = [ [1,2,3] ]

# matrix = [ [9], [8], [7] ]

matrix=[
    [5, 6, 3, -3, 12],
    [-3, 6, 5, 2, -1],
    [0, 0, 3, 12, 3]
  ]



Solution2(matrix)