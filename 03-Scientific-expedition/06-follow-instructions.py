from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:

    b = sum([ 1 for i in instructions if i == "f"  ]) 
    b += sum([ -1 for i in instructions if i == "b"  ]) 
    a = sum([ 1 for i in instructions if i == "r"  ]) 
    a += sum([ -1 for i in instructions if i == "l"  ]) 

    return (a,b)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
