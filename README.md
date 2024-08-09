# Abdulrahman-Duplicate-Files-Check
 Python program to traverse directory and locate files with duplicate content.

## Scenario
 As a developer, understanding the scenario is very important when it comes to developing a project. The scenario I created to be on theme with Lucasfilm is:
 > And sometimes all it requires is the will to jump. - Anakin Skywalker
 Anakin and Obi-Wan are on hot pursuit of General Grievous from an intense battle.
 Before leaving in his own escape pod, Grievous instructs a droid soldier to upload a virus to the pod computer system, adding extra files to the computers directory.
 Tasked with aiding the Jedi Knight and Jedi General, I was tasked with creating a python script to traverse the computer's file system and locate the ill-intented files.
 The indicator for the virus files are duplicate files uploaded by the droid.

## Assessment

Problem: Write a program that finds any files that contain duplicate contents within a directory tree.  
Input:  A directory path
Output:  Groups of paths to files that have the same contents
### NOTE: Code was tested on windows machine, formatted paths may be formatted differently depending on OS.
## Instructions
 To run the program, enter the directory in terminal/command prompt.
 Enter the command to run python with file 'main.py' attached Ex 'python3 main.py'
 Program will prompt you for a directory path from current location. If invalid input, program will reinquire.
 Upon successfull completion, the program will display the groups of files in separate lines in a list format.
 Program will give user the option to continue or terminate. Continuing will reloop to directory path specification.
#### Example inputs:
- python3 main.py
- ./tests/test-1
- No

## Assumptions
 - Program tested on python 3
 - There are only files openable with python's open function
 - We will have access to all files within the function
 - User will interact in console
 - no loop directories in folder system

## Format
 - Main.py: main method running full script
 - functions.py: important functionality for script
 - tests.py: unit tests of program
 - tests directory: example directories for program.

## Tests
In the main directory of the repository, a folder named tests has the example tests used on this program.
Due to time constraints two unit tests were included in the tests.py file. To run the file type the command 'python3 tests.py'.
### NOTE: Code was tested on windows machine, tests may be formatted differently on differing os.
1. ./tests/test-1
    - Duplicated files: test 1, test 2
    - Unique files: test 3
2. ./tests/test-2
    - Duplicated files: duplicate 1, duplicate 2, duplicate 3, duplicate 4 
    - Unique files: Unique.json
3. ./tests/test-3
    - Empty directory no duplicate files
4. ./tests/test-4
    - Both files are unqiue: hello.txt, helloWithSpace.txt
5. ./tests/test-5
    - Duplicated files: (duplicate v1, duplicate v2), (duplicate 3, duplicate 4) 
6. ./tests/test-6
    - This is not a directory, the file will raise an error to the user and ask for a valid test case

## Thought process
 Brainstorming led me to this idea

 First step, getting user input and validating the location to a directory
 Second step, traversing the located directory.
 Third step, finding the duplicate values of files.
 Final step, testing + validation
 30 minutes on user input, 45 minutes on functionality, 25 minutes on testing and validation

## Enhancements
 Due to time constraints I was not able to make the program as responsive as possible. These are the enhancements I would make:

 - Better test case coverage, I was only able to make unit tests for the traversal feature and some situations were not covered in time
 - Hashing the file values. The python hash function does cause some dataloss so I was afraid content of the files would be lost, python does have better hashing functions but with my limited time, full comparisons would be something that the program would store. Fundamentally increasing space and time complexity.
 - A UI would be nice, interacting with the console causes difficulty when it comes to testing compared to a native UI. I approached the problem from a UI pov, how would our user want the program to interact.