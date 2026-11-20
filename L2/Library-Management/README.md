# Library Management with Linked-Lists and Hash Table

## Description
In this C project (GCC compiler), the goal is to compare two different ways to implement a Library with multiple functions to manage it (like register x-lines of a text file, erase it, search...). You can use the makefile to compile directly.

- The first way of implement the Library is by using simple linked-lists structure.
- The second way is to implement it with a hash table (with a hash function and linked-lists again but not as the first way.)

In the hash table Library directory, you can decide which mode (hash table or linked-list) you want to use to implement your Library by putting a "H" or not at the end of your command on the Terminal. In fact, the codes of the first directory is present in the second.

The thing is to observe that the Library implemented with a hash table is way more efficient, due to its average-case complexity in O(1) for the search function for instance.
