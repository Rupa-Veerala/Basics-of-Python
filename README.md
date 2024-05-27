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
