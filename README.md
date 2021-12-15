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


### 4. First Fit Room
You are given a list of integers `rooms` and an integer `target`. Return the first integer in `rooms` that's `target` or larger. If there is no solution, return `-1`.

**Constraints**\
`0 ≤ n ≤ 100,000` where `n` is the length of `rooms`

**Example 1**

Input\
`rooms = [15, 10, 30, 50, 25]`
`target = 20`

Output\
`30`

Explanation\
`30` is the first room that's at least as large as `20`.

**Example 2**

Input\
`rooms = [15, 10, 30, 50, 25]`
`target = 51`

Output\
`-1`

Explanation\
There's no room that's at least `51`.

### 5. Odd Number of Digits
Given a list of positive integers `nums`, return the number of integers that have odd number of digits.

**Constraints**\
`n ≤ 100,000` where `n` is the length of `nums`

**Example 1**

Input\
`nums = [1, 800, 2, 10, 3]`

Output\
`4`

Explanation\
`[1, 800, 2, 3]` have odd number of digits.