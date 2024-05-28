**Installation**

Visit https://www.python.org/downloads/

Click on download

An exe file will be downloaded

Open it.

Click the add to Path checkbox

Install

Testing Installation

Open CMD

Type ‘python’ and press enter.

If there is no error, you are good to go.

**HISTORY OF PYTHON:**

-->Developed by Guido van Rossum in 1991.

-->It was originally developer to be the successor to ABC programmin language.

**FEATURES OF PYTHON**

-->Python is very easy to learn and code, and syntax in python is super easy to remember.

-->It is free and open source.

-->It is object oriented language.

**APPLICATIONS OF PYTHON:**

-->game development, machine learning, web development, Banking etc.

**VARIBLES:**

1).Variables are just containers to store data & variable names are just labels to those containers.

2). Many times, it is required to store this data in the program temporarily. For this purpose, we create variables.

3). There are certain rules to name a variable a) Starts with underscore( _ ) and letters only. (Letters include a,b,c, .z and A,B,C, .Z) b) Contains only letters, numbers and underscore.

**DATATYPES:**

All data elements need containers i.e. variables to be stored but the type of those containers can be very different due to the kind of data that is being stored. Following are the types of data based on various properties a) Numeric Integer: To store integers Eg: 2, -1

Float: To store numbers with decimal Eg: 3.4,9.7

Complex: To store numbers with real and imaginary part Eg: 4+3j

b) Boolean: To store result of expressions with results in either True or False.

c) Sequential

d) Sets

Strings, Tuples, Lists.

e) Dictionaries

**TYPECASTING**

-->Type casting means type conversion.

-->Two types of conversion

Implict typecasting: Happens conversions without our intervention.

Eg: a = 3 Here, a is automatically made into an int by assigning 3 into it.

EXplict Typecasting: requires our intervention.

Eg: b = 3.14

**COMMENTS**

Comments are used mainly in two cases a) To avoid a line of code from running/executing b) To avoid description of a code from being treated as code and executed. There are two types of comments a) Single line comments ( # ) Eg: #a = 3

b) Multi line comments ( “”” “”” )

Eg: “”” a = 3 b = 6 “”

Input

To get some data from the user.

input() functionality is used

By default, data received using input() is of string data type. It can be converted into the required data type by typecasting.

To convey the purpose of this data input to the user, we can pass string to the input()

Eg: a = input(‘Enter a number’)

Output

To display data to the user.

print() functionality is used.

We can pass any type of data to the print() function.

We can even pass multiple data elements at once.

a) Eg: print(a,b)

Parameter ‘end’ can be used to specify how the output should end. a) Eg: print(‘Hello’,end=’ ’)

Parameter ‘sep’ can be used to specify how the multiple data elements

passed have to be separated.

a) Eg: print(a,b,sep=’\n’)

**Operators**

Arithmetic operators +, -, *, /, %, **, //

Assignment operators

=, +=, -=, *=, /=, and so on

Comparison operators

, <, >=, <=, ==, !=

4)Logical operators

and, or, not

Bitwise operators &, |, ^, ~, >>, <<

**Precedence**

Shortcut---> PEMDAS

highest---()

p--> Parenthess

E--> Exponential

M--> Multiplication

D--> Division

A--> Addition

S--> Subtraction

**CONDITIONAL STATEMENTS**

These are used when you need to do something depending on whether or not a condition is satisfied.

We use if, elif, else keywords are used to implement the conditionals in python.

Syntax:

if condition1:

statements-to-execute when condition1 is satisfied

elif condition2:

statements-to-execute when condition1 is not satisfied & condition2 is satisfied

else:

statements-to-execute when none of the conditions are satisfied

After every : we are giving space, this is called indentation. Indentation is used to make sure that all required statements that are to be executed when condition is satisfied are grouped.

Note: Irrespective of the condition being satisfied or not, the code outside the indentation will always be executed.

**LOOPS**

These are used when you need to do something repeatedly.

It is really important to make sure that the repetition is not infinite. We can ensure this by -

a) Using a condition, until it is true, the loop will continue.

b) Making sure that condition is not true forever.

while, for keywords are used to implement the loops in python.

Syntax:

while condition:

statements-to-execute until condition is satisfied

for i in collection:

statements-to-execute until collection is not fully traversed

We can range() to generate a collection on the go in the following way- a) range(end)

b) range(start, end)

c) range(start, end, step_size)

note: end is not included in the collection.

After every : we are giving space, this is called indentation. Indentation is used to make sure that all required statements that are to be executed under a loop are grouped.

**break & continue**

These are keywords.

These are generally used in loops.

break - makes the execution complete exit the loop

continue - makes the execution skip the current iteration/repetition only.

**pass statement**

The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored.

The pass statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user simply places pass there as empty code is not allowed in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.

**Strings**

These are collections of characters.

Characters can be anything like letters, numbers, special characters.

**Lists & Tuples**

list and tuple are collection based datatypes.

list and tuple can store any type of datatypes like int, float, complex.

4-properties:

             list           tuple
ordered ---- Yes Yes

Indexed ---- Yes Yes

Mutable ---- Yes NO

Duplicate allowed ---- Yes Yes

Modifable --- Yes No

Mutable means we can change.

immutable means we can't change once created.

if it is ordered means automatically it is indexed.

not ordered means not indexed.

list indicated as []

tuple indicated as ()

we can't assign any value in tuple.

we can add values in list.

**Sets and Dictonaries**

4-properties:

           Set             Dict
ordered ---- No Yes

Indexed ---- No Yes

Mutable ---- No Yes

Duplicate allowed ---- No No

dict is 3.6 version and earlier are unordered

After 3.7 it is ordered.

In dict comparsion won't be possible.

dict is a collection of keys values pair.

{ : }

set {}

**Functions**

function--> Group/block of code.

**Recursion**

A function calling itself is called recursion.

In looping recursion will happen.

                  **This repository all about basics of Python upto Recursion** 

                            **Prepared by Rupa 🤍**
