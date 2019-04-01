# TODO: Add tests, fill in details, and make algorithm more readable

# Time Complexity:
# Space Complexity:
def stairs(n: int) -> int:
    """
    """
    if n == 1 or n == 2: return n
    if n == 3: return 4
    
    a, b, c, = 4, 2, 1
    for _ in range(n-3):
        a, b, c = a + b + c, a, b
    
    return a

