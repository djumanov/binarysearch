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

### 6. A Unique String
Given a lowercase alphabet string `s`, determine whether it has all unique characters.

**Constraints**\
`0 ≤ n ≤ 100,000` where `n` is the length of `s`

**Example 1**

Input\
`s = "abcde"`

Output\
`True`

Explanation\
All characters only occur once

**Example 2**

Input\
`s = "aab"`

Output\
`False`

Explanation\
There's two `a`s

**Example 3**

Input\
`s = ""`

Output\
`True`

Explanation\
All characters occur once (of which there are none)

### 7. FizzBuzz
Given an integer `n`, return a list of integers from `1` to `n` as strings except for multiples of `3` use `“Fizz”` instead of the integer and for the multiples of `5` use `“Buzz”`. For integers which are multiples of both `3` and `5` use `“FizzBuzz”`.

**Constraints**\
`0 ≤ n ≤ 100,000`

**Example 1**

Input\
`n = 15`

Output\
`["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]`

### 8. Largest Gap
Given a list of integers `nums`, return the largest difference of two consecutive integers in the sorted version of `nums`.

**Constraints**\
`n ≤ 100,000` where `n` is the length of `nums`

**Example 1**

Input\
`nums = [4, 1, 2, 8, 9, 10]`

Output\
`4`

Explanation\
The largest gap is between `4` and `8`.

### 9. Intervals Intersecting at Point
You are given a two-dimensional list of integers `intervals` and an integer `point`. Each element contains `[start, end]` represents an inclusive interval.

Return the number of intervals that are intersecting at `point`.

**Constraints**
`n ≤ 100,000` where `n` is the length of `intervals`

**Example 1**

Input\
`intervals = [
    [1, 5],
    [3, 9],
    [4, 8],
    [10, 13]
]`
`point = 4`

Output\
`3`

Explanation\
At time `4`, there are `3` intervals that are intersecting: `[1, 5], [3, 9], [4, 8]`

### 10. Reverse Words
Given a string `s` of words delimited by spaces, reverse the order of words.

**Constraints**
`n ≤ 100,000` where `n` is the length of `s`

**Example 1**

Input\
`sentence = "hello there my friend"`

Output\
`"friend my there hello"`

### 11. Length of a Linked List
Given a singly linked list node, return its length. The linked list has fields next and val.

**Constraints**
`n ≤ 100,000` where `n` is the number of nodes in `node`

**Example 1**

Input\
`node = [5, 4, 3]`

Output\
`3`

Explanation\
This linked list has `3` nodes.

**Example 2**

Input\
`node = [1, 2]`

Output\
`2`

Explanation\
This linked list has `2` nodes.