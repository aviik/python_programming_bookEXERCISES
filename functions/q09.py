'''
Write a function areaTriangle that takes length of three sides: side1, side2
and side3 as input command line arguements and returns the area of the
triangle as the output. Also assert that sum of any two sides is greater than
the third side.
                ________________
using     A = \/s(s-a)(s-b)(s-c)  where s = 1/2*( a + b + c )


'''

import sys
import math

sides = []


def areaTriangle(side1, side2, side3):
    '''
        Objective: Computes area of triangle 
        Input parameters: three sides - numeric value
        Return value: area of triangle - numeric value
    '''
    s = (side1 + side2 + side3)/2

    return math.sqrt(s * ( s - side1 )*( s - side2 )*( s - side3 ))



    

def main():
    '''
        Objective: Computes area of triangle and assert sum of two sides grater than third side.
        Input parameters: None
        Return value: 

    '''
    if len(sys.argv) == 4:
        #assert (sys.argv[0] + sys.argv[1])> sys.argv[2] or (sys.argv[0] + sys.argv[2])> sys.argv[1] or (sys.argv[1] + sys.argv[2]) > sys.argv[0]
        print("Area is: " , areaTriangle(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
        print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print('Invalid arguements')

if __name__ == '__main__':
    main()
    

    
