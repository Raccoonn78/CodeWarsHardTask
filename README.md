# CodeWarsHardTask


## hooks()
### Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

  Examples  
  "()"              =>  true  
  ")(()))"          =>  false  
  "("               =>  false  
  "(())((()())())"  =>  true  
Constraints  
  0 <= input.length <= 100  

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).  


##find_it
###Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples  
[7] should return 7, because it occurs 1 time (which is odd).  
[0] should return 0, because it occurs 1 time (which is odd).  
[1,1,2] should return 2, because it occurs 1 time (which is odd).  
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).  
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).  

