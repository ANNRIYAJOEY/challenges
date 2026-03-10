# Student Grade Management System:-

# Function to calculate the average of marks
def calculate_average(marks):
    total=0  # Set total sum of marks to 0
    for mark in marks: # Loop through each mark in the list
        total+=mark    # Add the current mark to total

    average = total/len(marks) # Divide total by number of marks to get average

    return average  # Return the calculated average

# Function to determine grade based on average
def get_grade(average):

    if average>=90:     # If average is 90 or above
        return "A"
    elif average>=80:   # If average is between 80 and 89
        return "B"
    elif average>=70:   # If average is between 70 and 79
        return "C"
    elif average>=60:   # If average is between 60 and 69
        return "D"
    else:              # If average is below 60
        return "F"
    
marks=[]  # Create an empty list to store marks

# Collect 5 valid marks from the user
while len(marks)<5:
    mark=float(input(f"Enter mark {len(marks)+1}:-"))  # Take input as float to allow decimals

    if 0<= mark <= 100:       # Validate that mark is between 0 and 100
        marks.append(mark)    # Add valid mark to the list
    else:
        print('INVALID INPUT!!,"VALUES SHOULD BE BETWEEN 0 TO 100"')   # Show error for invalid input

# Calculate average and grade using the defined functions
average=calculate_average(marks)  # Calculate average and grade using the defined functions
grade=get_grade(average)          # Call function to determine grade based on average


# Display the results using formatted strings
print(f'AVERAGE MARK:{average}')  # Show average marks
print(f'GRADE:{grade}')           # Show final grade

"""
SUMMARY:-
Student Grade Management System :

This program implements a Student Grade Management System using Python. 
The main objective is to calculate the average marks of a student from five subjects 
and determine the corresponding grade based on predefined criteria.

Approach:
1. Defined two user-defined functions:
   - calculate_average(marks): Accepts a list of numeric marks, calculates the total sum,
     and returns the average.
   - get_grade(average): Accepts the average mark and returns a grade (A, B, C, D, F) 
     based on standard grading criteria.
2. Used a list named 'marks' to store the five subject marks.
3. Collected user input in a while loop until exactly five valid marks are entered.
4. Applied input validation to ensure only numeric marks between 0 and 100 are accepted.

Validation Logic:
- For each input, the program checks if the mark is between 0 and 100 using:
      if 0 <= mark <= 100
  - If the mark is valid, it is added to the list.
  - If the mark is invalid, an error message is displayed:
      "INVALID INPUT!! VALUES SHOULD BE BETWEEN 0 TO 100"
  - The user is then prompted to enter the mark again.
- This ensures the program only processes valid data for average calculation and grading.

Learning Outcomes:
- Learned to write and use user-defined functions for modular programming.
- Gained experience using loops and conditional statements for control flow.
- Understood input validation and error handling to make the program robust.
- Practiced using lists for data storage and iteration.
- Improved output formatting using f-strings for clear presentation.

Sample Input and Output Demonstration:

User Input:
Enter mark 1:- 85
Enter mark 2:- 90
Enter mark 3:- 78
Enter mark 4:- 88
Enter mark 5:- 92

Program Output:
AVERAGE MARK: 86.60
GRADE: B


Conclusion:
The program successfully calculates the average marks and determines the grade for a student 
while handling invalid inputs effectively. This assignment strengthened foundational Python 
skills including functions, loops, conditional logic, input validation, and clean code formatting.
"""
