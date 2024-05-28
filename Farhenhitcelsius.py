"""Problem statement
Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E), and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W into their corresponding Celsius values and print the table.

Note:
Print the floor of the Celsius values if they are non-negative else print its ceil value. 
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
0 <= S <= 80
S <= E <=  900
0 <= W <= 40 
Sample Input 1:
0 
100 
20
Sample Output 1:
0   -17
20  -6
40  4
60  15
80  26
100 37"""


S = int(input())
E = int(input())
W = int(input())
for c in range(S,E+1,W):
    celsi = int((c-32)*5/9)
    print(c,celsi,sep="\t")