'''
The prime factors of 13195 are 5, 7, 13 and 29
What is the largest prime factor of a given number N?

Input Format:
First line contains T,the number of test cases. This is followed by T lines each containing an integer N.

Constraints:
1 <= T <= 10
10 <= N <= 10**12

Output Format:
For each test case, display the largest prime factor of N.

Sample Input 0:
2
10
17

Sample Output 0:
5
17
'''

import sys, math


def n_is_prime(n):
    if n == 2 or n == 3:
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    j = 5
    while (j*j <= n):
        if (n % j == 0 or n % (j+2) == 0):
            return False
        j += 6
    
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n_is_prime(n) or n == 1:
        print(n)
    else:
        lst = []
        # Check for divisibility by 2
        while n % 2 == 0: 
            lst.append(2)
            n = n / 2

        for val in range(3,int(math.sqrt(n))+1, 2): 
            while n % val == 0: 
                lst.append(val)
                n = n / val
        
        if n > 2:
            lst.append(n)
        print(int(max(lst)))
