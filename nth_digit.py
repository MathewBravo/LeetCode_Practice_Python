def findNthDigit(n: int) -> int:
    # Initialize some variables
    start, size, step = 1, 1, 9
    
    # Find the range where the nth digit falls into
    while n > size * step:
        n -= size * step
        start *= 10
        size += 1
        step *= 10
    
    # Find the actual number in that range
    num = start + (n - 1) // size
    
    # Calculate the position of the nth digit in the number
    position = (n - 1) % size
    
    # Convert the number to a string and return the nth digit
    return int(str(num)[position])
