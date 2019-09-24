'''
CODCHESS

For all odd sizes of the ‘maidaans'(chessboards) A will win and B will win in rest of the cases.
'''
for tc in range(int(input())): 
    print (1 - int(input())%2)
