#RANJAN02 - Tower Of Hanoi - Revisited -
#Find the shortest sequence of moves that transfers a tower of n disks from the left peg A to the right peg C,
'''
Constraints:
1. Initially the left peg A in stacked by n disks in the order of decreasing size.
2. if direct moves between A and C are disallowed. (Each move must be to or from the middle peg B.)
3. Only one move cand be done at a time and never moving a larger one onto a smaller.
4. u can only move one disk as a time

For 2 disk, 8 moves were required
for 3 disk, 26 moves were required --> means solution is-->(3**no of disk - 1)
'''

for tc in range(int(input())): print (3**int(input()) - 1)
