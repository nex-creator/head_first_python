def square_root_bisection(number,tolerance=0.01, max_iterations=100):
    if number < 0:
        raise ValueError("Cannot compute square root of negative number")
    if number == 0  or number == 1:
        print(f'The square root of {number} is {number}')
        return number
    if 0 < number < 1:
        low = number
        high = 1
    else:
        low = 1
        high = number
    iterations = 0
    while (high-low) >= tolerance and iterations < max_iterations:
        mid = (low + high) / 2
        mid_square = mid * mid
        if abs(mid_square-number) < tolerance:
            print(f'The square root of {number} is approximately {mid}')
            return mid
        elif mid_square < number:
            low = mid
        else:
            high = mid
        iterations += 1
    print(f'Failed to converge within {max_iterations} iterations')
    return None

square_root_bisection(35, tolerance=0.0001)
