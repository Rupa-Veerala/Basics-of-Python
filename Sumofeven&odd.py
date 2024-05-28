"""Problem statement
Write a program to input an integer N and print the sum of all its even digits and all its odd digits separately.

Digits mean numbers, not the places! If the given integer is "13245", the even digits are 2 and 4, and the odd digits are 1, 3, and 5.

Detailed explanation ( Input/output format, Notes, Images )
Constraints
0 <= N <= 10^8
Sample Input 1:
1234
Sample Output 1:
6 4
Sample Input 2:
552245
Sample Output 2:
8 15"""


N = input()
even = 0
odd=0
for i in N:
    if int(i)%2==0:
        even = even+int(i)
    else:
        odd = odd+int(i)
print(even,odd)