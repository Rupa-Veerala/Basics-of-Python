"""Problem statement
Take the principal amount, rate of interest, and the time period as input and calculate the Simple Interest.

Note: Return answer as Floor integer value.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
2000
2.2
4
Sample Output 1:
176
Explanation of Sample Input 1:
The input is principal=2000, rate=2.2 and time=4.
So Simple interest=Principal*rate*time/100 hence 
answer is 2000*2.2*4/100=176"""

p = int(input())
r = float(input())
t = int(input())
si=p*t*r//100
print(int(si))
