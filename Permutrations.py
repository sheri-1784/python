from time import sleep
def cls():
    print('\033[2J\033[;H',end='')
    sleep(0.1)
cls()

Recursion
---> Exhaustive search
"13
136, 163, 316, 361, 613, 631
316, 361, 613, 631

whose first digit is divisible by 3
All possible permutations = 123, 132, 213,231, 312, 321

Give me permutation strings which are either sorted in ascending or descending order.

Method#1
    - Generate all permutations, and check them one by one. 128 + 128 = 256*n
Method#2
    - 1/2/4/5/7/8/ --> return --> X strings would not be generated in this case.



123 -->
132 --> 1 + F(23) {23, 32}
123. 132


F (23)
132
-> 2 3
-> 3 2
2 + (left + right)
2 + 13
213
231
=-> 2 + F (13)
--------------
3 + left = 12, right = " "
3+F(12）= 312, 321

"a"
"ab"
"abc"

- Generate all permutations of a string. permute("abc").
    All output strings are of size. All permutations
- Generate all combinations of a string. combination("abc")
    + {{}. a, b, c, ab, ac, bc, abc} PowerSet

