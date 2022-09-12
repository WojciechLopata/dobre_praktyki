import numpy as np
piece=[[0,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]
piece=[[0,0,0,0],[0,0,0,0],[0,1,1,1],[0,0,0,1]]
#rotated = list(zip(*a[::-1]))

def print2_d(piece):
    for line in piece:
        print(line)
    print("--------------------------------------------------------")
        
#piece_rotated=[[0,0,0,0],[0,0,0,0],[0,1,1,0],[1,1,0,0]
ihm = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
ihm=np.array(ihm)
    
piece=np.array(piece)
piece.transpose()
rotation =np.matmul( piece,ihm)
piece=rotation
print(piece)
piece.transpose()
rotation =np.matmul( piece,ihm)
piece=rotation
print(piece)    
        
    #for i in lista:
 
     #   helper[i]

