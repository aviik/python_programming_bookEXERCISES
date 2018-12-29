'''
WRITE A FUNCTION areaTriangle that takes length of three sides: side1, side2
and side3 of the triangle as input parameters and returns the area of the
triangle as the output. Also assert that sum of any two sides is greater than
the third side.
Write a function main that acccepts inputs from the user interactively and
computes the area of the triangle using the function areaTriangle.


                ________________
using     A = \/s(s-a)(s-b)(s-c)  where s = 1/2*( a + b + c )

'''
import math

sides = []


def areaTriangle(side1, side2, side3):
    '''
        Objective: Computes area of triangle 
        Input parameters: three sides - numeric value
        Return value: area of triangle - numeric value
    '''
    s = 0.5 * (side1 + side2 + side3)

    return (math.sqrt(s * ( s - side1 )*( s - side2 )*( s - side3 )))



    

def main():
    '''
        Objective: Computes area of triangle and assert sum of two sides grater than third side.
        Input parameters: None
        Return value: 
    '''
    count = 1
    while count<=3:
        side = int(input (f'Enter length of side {count} : '))
        sides.append(side)
        count += 1
    assert (sides[0] + sides[1])> sides[2] or (sides[0] + sides[2])> sides[1] or (sides[1] + sides[2]) > sides[0]
    print("Area is: " , areaTriangle(sides[0],sides[1],sides[2]))

if __name__ == '__main__':
    main()

    
