from typing import Union 
import math 

def square_root(value:Union[int,float]=5):
    """Returns the square root of the given value

    Args:
        value (Union[int,float]): value to take square root - strictly must be an integer or a float and must be greater than 0
    Return:
        math.sqrt(value)
    """
    assert (isinstance(value,int) or isinstance(value,float)), "Input value must be integer or float!"
    
    if value < 0: #If the value is smaller than 0
        raise ValueError("Input value must be non-negative!")
    
    return math.sqrt(value)

if __name__ == "__main__":
    print(square_root(9))

    
    
    
    