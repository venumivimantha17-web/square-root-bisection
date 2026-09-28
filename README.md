# Square Root Bisection Method

A Python implementation of the bisection method for finding the square root of a number.

## Description

The bisection method is a numerical root-finding technique that repeatedly divides an interval into two parts to approximate a solution.

This project implements the bisection method to calculate the square root of a given number without using external Python modules.

## Features

- Calculates square roots using the bisection method.
- Supports a configurable tolerance value.
- Supports a configurable maximum number of iterations.
- Handles `0` and `1` directly.
- Raises a `ValueError` for negative numbers.
- Returns `None` if the calculation does not converge within the specified number of iterations.
- Requires no external Python modules.

## Function

```python
square_root_bisection(square_target, tolerance=1e-7, maximum=100)
