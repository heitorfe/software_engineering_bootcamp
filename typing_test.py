from typing import Union, Optional

def test_function(a : int) -> int:
    return a

def division(a: int, b: Optional[int]) -> Optional[float]:
    if b is None:
        return a

    if b != 0:
        return a / b
    


return_val = test_function([1])
print(return_val)
print((division(1, None)))