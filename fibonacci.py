"""
FIBONACCI SEQUENCE - Three Implementation Approaches
====================================================
Fibonacci: Each number is the sum of the two preceding ones
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

Mathematical definition:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n > 1
"""

# ==============================================================================
# APPROACH 1: NAIVE RECURSION (Top-Down)
# ==============================================================================
def fibonacci_recursive(n: int) -> int:
    """
    Calculate nth Fibonacci number using pure recursion.
    
    Time Complexity: O(2^n) - Exponential (VERY SLOW!)
    Space Complexity: O(n) - Call stack depth
    
    PROS:
        - Simplest to understand
        - Matches mathematical definition exactly
        - Clean, elegant code
    
    CONS:
        - Extremely slow for n > 35
        - Recalculates same values many times
        - Stack overflow risk for large n
    
    WHEN TO USE:
        - Teaching/learning recursion concepts
        - n is very small (< 20)
        - Code clarity is more important than performance
    
    INTERVIEW TIP:
        - Always mention the time complexity problem
        - Follow up by explaining memoization could fix it
    """
    # Base cases: fib(0) = 0, fib(1) = 1
    if n == 0 or n == 1:
        return n
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ==============================================================================
# APPROACH 2: TOP-DOWN WITH MEMOIZATION (Dynamic Programming)
# ==============================================================================
def fibonacci_memoization(n: int, memo: dict = None) -> int:
    """
    Calculate nth Fibonacci number using recursion with caching.
    
    Time Complexity: O(n) - Each value calculated once
    Space Complexity: O(n) - Cache storage + call stack
    
    PROS:
        - Much faster than naive recursion
        - Still uses recursive logic (intuitive)
        - Automatically handles visited subproblems
    
    CONS:
        - Extra memory for cache
        - Still has recursion overhead
        - May hit recursion limit for very large n
    
    WHEN TO USE:
        - Need recursive approach but with good performance
        - Problem has overlapping subproblems
        - Not all subproblems may be needed
        - Medium to large n (up to ~1000)
    
    INTERVIEW TIP:
        - This is often the "optimal" recursive solution interviewers want
        - Demonstrates understanding of Dynamic Programming
    """
    # Initialize memo dictionary on first call
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 0 or n == 1:
        return n
    
    # Check if already calculated (memoization magic!)
    if n in memo:
        return memo[n]
    
    # Calculate and store in cache before returning
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# ==============================================================================
# APPROACH 3: BOTTOM-UP WITH FULL SEQUENCE (Iterative DP)
# ==============================================================================
def fibonacci_sequence(n: int) -> list:
    """
    Calculate Fibonacci sequence from 0 to n using iteration.
    Returns the entire sequence as a list.
    
    Time Complexity: O(n) - Single loop
    Space Complexity: O(n) - Stores entire sequence
    
    PROS:
        - No recursion (no stack overflow)
        - Can access any previous value
        - Good for visualization/debugging
        - Returns complete sequence
    
    CONS:
        - Uses O(n) memory even if you only need last value
        - Slightly more memory than necessary
    
    WHEN TO USE:
        - Need the entire Fibonacci sequence, not just one value
        - Want to display/return multiple values
        - Learning and visualization
        - Need to access any fib(k) for k <= n later
    
    INTERVIEW TIP:
        - Good for problems that ask for "all Fibonacci numbers up to n"
        - Shows you understand arrays/lists
    """
    # Handle edge cases
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    # Initialize with base cases
    sequence = [0, 1]
    
    # Build up the sequence
    for i in range(2, n + 1):
        next_val = sequence[i - 2] + sequence[i - 1]
        sequence.append(next_val)
    
    return sequence


def fibonacci_sequence_value(n: int) -> int:
    """
    Returns just the nth Fibonacci number using sequence approach.
    Wrapper around fibonacci_sequence for single value queries.
    """
    if n == 0 or n == 1:
        return n
    
    sequence = [0, 1]
    
    for i in range(2, n + 1):
        next_val = sequence[i - 2] + sequence[i - 1]
        sequence.append(next_val)
    
    return sequence[n]  # Return only the nth value


# ==============================================================================
# APPROACH 4: BOTTOM-UP OPTIMIZED (Most Efficient)
# ==============================================================================
def fibonacci_optimized(n: int) -> int:
    """
    Calculate nth Fibonacci number using iteration with O(1) space.
    This is the MOST EFFICIENT approach for single value queries.
    
    Time Complexity: O(n) - Single loop
    Space Complexity: O(1) - Only 2-3 variables
    
    PROS:
        - Fastest approach in practice
        - Minimal memory usage
        - No recursion (handles very large n)
        - Production-ready code
    
    CONS:
        - Slightly less intuitive than recursion
        - Can't access previous values once computed
        - Only returns single value
    
    WHEN TO USE:
        - Production code
        - Large values of n (even n > 10,000)
        - Memory constraints
        - Need best performance
        - Only need the nth value, not the sequence
    
    INTERVIEW TIP:
        - This is usually the "best" answer for Fibonacci
        - Shows you understand space optimization
        - Demonstrates iterative thinking
    """
    # Base cases
    if n == 0 or n == 1:
        return n
    
    # Only keep track of last two values
    prev2 = 0  # fib(i-2)
    prev1 = 1  # fib(i-1)
    
    # Build up from bottom
    for _ in range(2, n + 1):
        current = prev2 + prev1  # fib(i) = fib(i-2) + fib(i-1)
        
        # Shift values for next iteration
        prev2 = prev1  # Old prev1 becomes new prev2
        prev1 = current  # Current becomes new prev1
    
    return current


# ==============================================================================
# TESTING AND COMPARISON
# ==============================================================================
def compare_approaches(n: int):
    """
    Compare all approaches for a given n.
    Useful for understanding differences.
    """
    print(f"\n{'='*60}")
    print(f"Fibonacci({n}) - Comparing All Approaches")
    print(f"{'='*60}")
    
    # Approach 1: Naive Recursion
    result1 = fibonacci_recursive(n)
    print(f"1. Naive Recursion:     fib({n}) = {result1}")
    print(f"   Time: O(2^n), Space: O(n)")
    
    # Approach 2: Memoization
    result2 = fibonacci_memoization(n)
    print(f"2. Memoization:         fib({n}) = {result2}")
    print(f"   Time: O(n), Space: O(n)")
    
    # Approach 3: Bottom-up with sequence
    sequence = fibonacci_sequence(n)
    print(f"3. Full Sequence:       {sequence}")
    print(f"   Time: O(n), Space: O(n)")
    
    # Approach 4: Optimized
    result4 = fibonacci_optimized(n)
    print(f"4. Optimized:           fib({n}) = {result4}")
    print(f"   Time: O(n), Space: O(1) ★ BEST")
    
    print(f"{'='*60}\n")


# ==============================================================================
# INTERVIEW CHEAT SHEET
# ==============================================================================
"""
QUICK REFERENCE FOR INTERVIEWS:
================================

QUESTION: "Implement Fibonacci"
DEFAULT ANSWER: fibonacci_optimized() - O(n) time, O(1) space

QUESTION: "Return all Fibonacci numbers up to n"
ANSWER: fibonacci_sequence() - O(n) time, O(n) space

QUESTION: "Implement recursively"
ANSWER: fibonacci_memoization() - O(n) time, O(n) space
MENTION: Naive recursion is O(2^n) and should use memoization

FOLLOW-UP QUESTIONS TO EXPECT:
- "What's the time complexity?" → Always analyze and state it
- "Can you optimize space?" → Show the two-variable approach
- "What about very large n?" → Mention iteration over recursion

COMMON MISTAKES TO AVOID:
- Using naive recursion without mentioning its inefficiency
- Not handling base cases (n=0, n=1)
- Off-by-one errors in loop ranges
- Index errors when building sequence

PRO TIPS:
- Always mention trade-offs (time vs space, clarity vs efficiency)
- Start with a working solution, then optimize
- Draw out the first few values to verify logic
- Test edge cases: n=0, n=1, n=2
"""


# ==============================================================================
# MAIN - TEST ALL APPROACHES
# ==============================================================================
if __name__ == "__main__":
    # Test with small value
    compare_approaches(10)
    
    # Individual tests
    print("\nIndividual Tests:")
    print(f"Recursive fib(6) = {fibonacci_recursive(6)}")
    print(f"Memoized fib(6) = {fibonacci_memoization(6)}")
    print(f"Sequence fib(6) = {fibonacci_sequence_value(6)}")
    print(f"Optimized fib(6) = {fibonacci_optimized(6)}")
    
    # Large value (only safe with efficient methods)
    print(f"\nLarge value test:")
    print(f"Optimized fib(50) = {fibonacci_optimized(50)}")
    # Note: Don't try fibonacci_recursive(50) - it would take forever!

## Summary Table for Quick Reference
"""
METHOD              | TIME  | SPACE | BEST FOR
--------------------|-------|-------|---------------------------
Naive Recursion     | O(2ⁿ) | O(n)  | Learning, n < 20
Memoization         | O(n)  | O(n)  | Recursive + Fast
Sequence (full)     | O(n)  | O(n)  | Need all values
Optimized (2 vars)  | O(n)  | O(1)  | Production, single value

"""