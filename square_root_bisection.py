def square_root_bisection(square_target, tolerance=1e-7, maximum=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    lower_bound = 0
    upper_bound = max(1, square_target)

    for _ in range(maximum):
        midpoint = (lower_bound + upper_bound) / 2

        if upper_bound - lower_bound <= tolerance:
            print(
                f"The square root of {square_target} is approximately {midpoint}"
            )
            return midpoint

        if midpoint * midpoint < square_target:
            lower_bound = midpoint
        else:
            upper_bound = midpoint

    print(f"Failed to converge within {maximum} iterations")
    return None
