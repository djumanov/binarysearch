# binarysearch
## easy-level
### 1. Sum of First N Odd Integers
Given an integer n, return the sum of the first n positive odd integers.

**Constraints**\
`n ≤ 1,000`

**Example 1**

Input\
`n = 5`

Output\
`25`

**Explanation**
The first `5` odd integers are `[1, 3, 5, 7, 9]` and its sum is `25`.

### 2. Check Palindrome
Given a string s, return whether it is a palindrome.

**Constraints**\
`n ≤ 100,000 `where `n` is the length of `s`

**Example 1**

Input\
`s = "racecar"`

Output\
`True`

**Example 2**

Input\
`s = "evilolive"`

Output\
`True`

**Example 3**

Input\
`s = "palindrome"`

Output\
`False`

### 3. Collatz Sequence
Given a positive integer n, find the length of its Collatz sequence. The Collatz sequence is generated sequentially where

- `n = n / 2` if `n` is even
- `n = 3 * n + 1` if `n` is odd
- And the sequence ends if `n = 1`

**Example 1**

Input\
`n = 11`

Output\
`15`

Explanation\
The Collatz sequence is: `[11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]` and its length is `15`.