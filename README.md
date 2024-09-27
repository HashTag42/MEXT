# Exercise

__Complete the following exercise__

Write a Test Plan and detail the Test Suites/Cases to qualify for delivery the following application. The Test Plan
 contains all Test Suites/Cases, the sequence in which they are used and the criteria for delivering the application.
 The Test Suites/Cases contain all pass/fail criteria and the data required to determine pass/fail. Pseudo (or python)
 code is desired for each Test Case.

__*Application Triangle_Classifier:*__

Inputs: new line separated strings. Words in a string are separated by white space. WHEN there are three separate words
 in a string, AND when each word is a number, then the application outputs one word.

Outputs: one word from the set of words	[“Scalene”,”Isosceles”,”Equilateral”,”NoTriangle”] on stdout. Error strings on
 stderr.

Operation: The choice of the output word is made by interpreting each number as a length of a side of a triangle. In ALL
 OTHER cases the output is an error string indicating that the input could not be classified. The error string also
 indicates the cause of the error. Causes include what it is about the string that it cannot be classified OR execution
 errors. The program exits when the input string contains the word “Exit” or the word “Quit” at the beginning of the
 string.

__Examples:__

Input “1 1 1” Output “Equilateral”

Input “1” Output “Error: Two sides missing”

Input “Quit” Application exits.

___

# Solution

## Design

Create a program in Python to process each line of an input file into one of the triangle types, and write an error to
 stderr when the input cannot be classified as a triangle.

As a reminder, these are the types of triangles based on the length of their sides:

- Equilateral triangle: Three equal sides.
- Isosceles triangle: Two equal sides.
- Scalene triangle: No equal sides.

## Test Plan

- All tests will be automated. There will be no manual testing.
- All tests must pass before release.
- Positive test cases
	- Lines describing equilateral triangles (Three equal sides)
	- Lines describing isosceles triangles (Two equal sides)
	- Lines describing scalene triangles (No equal sides)
	- Lines with all sides using integer numbers greater than 0
	- Lines with all sides using floating-point numbers greater than 0
- Negative test cases
	- Lines with sides equal to 0
	- Lines with sides smaller than 0
	- Lines with more sides than 3
	- Lines with less sides than 3
	- Lines with no sides
	- Lines with sides using alpha values that cannot be converted to int or float
- Program termination
	- Lines with the keyword QUIT
	- Lines with the keyword EXIT

## Implementation

- README.md: This file.
- Triangle_Classifier.py: Main program file.
	- Process an input file to classify each line as a triangle.
	- Contains the Get_Triangle_Type() function that classifies triangles.
- inputs.txt: Sample input file.
- strings.py: Dictionary with all output strings.
- printError.py: Small function to writes to stderr
- Triangle_Classifier_test.py: Unit test runner.
	- Reads a fixtures file to generate a list of test cases to execute.
- fixtures.txt: List of unit tests to execute.

## Execution

__To run the main program:__

> `> python Triangle_Classifier.py input.txt`

__To run the unit tests:__

> `> python -m unittest Triangle_Classifier_test.py`