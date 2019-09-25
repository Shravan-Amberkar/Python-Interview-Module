#ROOTCIPH - Decipher
'''
Explanation
cubic polynomial--> x^3 + ax^2 + bx + c
Let the roots be x1, x2, x3
from the cubic equation property
x1+x2+x3 = -a
x1*x2+x2*x3+x1*x3 = b
x1*x2*x3 = -c
   
 let the coordinates be (x1,x2,x3)
 now the distance (r) is = sqrt(x1^2+x2^2+x3^2)
 square of distance =(x1^2+x2^2+x3^2) <--- to find
  
we know -->Square of a Trinomial is..
(x1+x2+x3)^2=(x1^2+x2^2+x3^2)+ 2*(x1*x2+x2*x3+x1*x3)
(x1^2+x2^2+x3^2)= (x1+x2+x3)^2 - 2*(x1*x2+x2*x3+x1*x3)

HENCE --> (x1^2+x2^2+x3^2)= (-a)^2 - 2*(b)
  
 Square of distance = a*a - 2*b

'''


for tc in range(int(input())):
    a, b, c = map(int,input().split())
    print (a*a - 2*b)
