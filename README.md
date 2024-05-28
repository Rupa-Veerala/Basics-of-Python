**Installation**

 1) Visit https://www.python.org/downloads/
 2) Click on download
 3) An exe file will be downloaded
 4) Open it.
 5) Click the add to Path checkbox
 6) Install
    
**Testing Installation**
 1) Open CMD
 2) Type ‘python’ and press enter.
 3) If there is no error, you are good to go.

**HISTORY OF PYTHON**:

-->Developed by Guido van Rossum in 1991.

-->It was originally developer to be the successor to ABC programmin language.

**FEATURES OF PYTHON**

-->Python is very easy to learn and code, and syntax in python is super easy to remember.

-->It is free and open source.

-->It is object oriented language.

**APPLICATIONS OF PYTHON**:

-->game development, machine learning, web development, Banking etc.

**VARIBLES**:

1).Variables are just containers to store data & variable names are just labels to
   those containers.

2). Many times, it is required to store this data in the program temporarily. For this
    purpose, we create variables.

3). There are certain rules to name a variable 
      a) Starts with underscore( _ ) and letters only. (Letters include a,b,c, .z and
         A,B,C, .Z)
      b) Contains only letters, numbers and underscore.

**DATATYPES**:

 1) All data elements need containers i.e. variables to be stored but the type of
 those containers can be very different due to the kind of data that is being
 stored.
 2) Following are the types of data based on various properties 
a) Numeric

 Integer: To store integers Eg: 2, -1
 
 Float: To store numbers with decimal Eg: 3.4,9.7
 
 Complex: To store numbers with real and imaginary part Eg: 4+3j
 
 b) Boolean: To store result of expressions with results in either True or False.
 
 c) Sequential
 
 d) Sets
 
 Strings,
 Tuples,
 Lists.
 
 e) Dictionaries

**TYPECASTING**

-->Type casting means type conversion.

-->Two types of conversion
1) Implict typecasting: Happens conversions without our intervention.

   Eg: a = 3 Here, a is automatically made into an int by assigning 3
   into it.
   
2) EXplict Typecasting:  requires our intervention.
   
 Eg: b = 3.14
 
 **COMMENTS**
 
 1) Comments are used mainly in two cases 
     a) To avoid a line of code from running/executing
     b) To avoid description of a code from being treated as code and
       executed.
 2) There are two types of comments 
a) Single line comments ( # )
 
 Eg: #a = 3
 
 b) Multi line comments ( “”” “”” )
 
 Eg: “”” a = 3
 b = 6 “”

**Input**

 1) To get some data from the user.
    
 2) input() functionality is used
    
 3) By default, data received using input() is of string data type. It can be
    converted into the required data type by typecasting.
    
 4) To convey the purpose of this data input to the user, we can pass string to the
 input()

 5) Eg: a = input(‘Enter a number’)
    
 **Output**
 
 1) To display data to the user.
    
 2) print() functionality is used.
    
 3) We can pass any type of data to the print() function.
    
 4) We can even pass multiple data elements at once.
    
 a) Eg: print(a,b)

 5) Parameter ‘end’ can be used to specify how the output should end.
    
 a) Eg: print(‘Hello’,end=’ ’)
 
 6) Parameter ‘sep’ can be used to specify how the multiple data elements
     
     passed have to be separated.
 
 a) Eg: print(a,b,sep=’\n’)

 **Operators**
 
 1) Arithmetic operators
    
   +, -, *, /, %, **, //
 
 2) Assignment operators
    
    =, +=, -=, *=, /=, and so on
 
 3) Comparison operators
    
   >, <, >=, <=, ==, !=
 
 4)Logical operators
 
   and, or, not
 
 5) Bitwise operators
    &, |, ^, ~, >>, <<

**CONDITIONAL STATEMENTS**

1) These are used when you need to do something depending on whether
  or not a condition is satisfied.

2) We use if, elif, else keywords are used to implement the conditionals in
python.

3) Syntax:
   
if condition1:

statements-to-execute when condition1 is satisfied

elif condition2:

statements-to-execute when condition1 is not satisfied & condition2 is satisfied

else:

statements-to-execute when none of the conditions are satisfied

4) After every : we are giving space, this is called indentation. Indentation
is used to make sure that all required statements that are to be
executed when condition is satisfied are grouped.

5) Note: Irrespective of the condition being satisfied or not, the code
   outside the indentation will always be executed.

**LOOPS**

1) These are used when you need to do something repeatedly.
   
2) It is really important to make sure that the repetition is not infinite. We
   can ensure this by -
   
a) Using a condition, until it is true, the loop will continue.

b) Making sure that condition is not true forever.

3) while, for keywords are used to implement the loops in python.
   
4) Syntax:
   
while condition:

statements-to-execute until condition is satisfied

for i in collection:

statements-to-execute until collection is not fully traversed

5) We can range() to generate a collection on the go in the following way-
   
a) range(end)

b) range(start, end)

c) range(start, end, step_size)

note: end is not included in the collection.

6) After every : we are giving space, this is called indentation. Indentation
is used to make sure that all required statements that are to be
executed under a loop are grouped.

 **break & continue**
 
 1) These are keywords.
   
 2) These are generally used in loops.
    
 3) break - makes the execution complete exit the loop
    
 4) continue - makes the execution skip the current iteration/repetition
    only.

**pass statement** 

The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored. 

The pass statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user simply places pass there as empty code is not allowed in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.

**Strings**

1) These are collections of characters.
   
2) Characters can be anything like letters, numbers, special characters.

**Lists & Tuples**

list and tuple are collection based datatypes.

list and tuple can store any type of datatypes like int, float, complex.

4-properties:

                     list           tuple
 
ordered ----         Yes             Yes

Indexed ----         Yes             Yes

Mutable ----         Yes             NO

Duplicate
allowed ----        Yes             Yes

Modifable ---       Yes             No

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

ordered ----         No             Yes

Indexed ----         No             Yes

Mutable ----         No             Yes

Duplicate
allowed ----        No              No

dict is 3.6 version and earlier are unordered

After 3.7 it is ordered.

In dict comparsion won't be possible.

dict is a collection of keys values pair.

{ :  }

set {}

**Functions**

function--> Group/block of code.




