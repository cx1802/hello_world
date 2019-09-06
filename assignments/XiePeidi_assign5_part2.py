"""
Peidi Xie
March 30th, 2019
Introduction to Programming, Section 03
Part 2: Dynamic Gradebook
"""

# prompt the user to enter the number of students in his or her class, and the number of tests in the class
# if the user doesn't anter a positive number, ask the user to enter again until the user supplies a positive number
num_students = int(input("How many students are in your class? "))
while num_students <= 0:
    print("Invalid # of students, try again.")
    print()
    num_students = int(input("How many students are in your class? "))

num_tests = int(input("How many tests in this class? "))
while num_tests <= 0:
    print("Invalid # of tests, try again.")
    print()
    num_tests = int(input("How many tests in this class? "))

# signify the start of the program
print()
print("Here we go!")

# prompt the user to enter scores for each tests of each students
# keep track of the total scores of each students and the total score of the entire class
totalscore_class = 0
for i in range(1, num_students+1):
    totalscore_student = 0
    print()
    print("**** Student #" + str(i) + "****")
    for f in range(1, num_tests+1):
        score = float(input("Enter score for test #" + str(f) + ": "))
        # if the user doesn't enter a positive score, ask the user to enter again until the user
        # supplies a positive score
        while score <= 0:
            print("Invalid score, try again")
            score = float(input("Enter score for test #" + str(f) + ": "))
        totalscore_student += score
    totalscore_class += totalscore_student
    # calculate the average scores for each students and display the average scores to the user
    average_student = totalscore_student / num_tests
    print("Average score for student #" + str(i) + " is " + format(average_student, ".2f"))

# calculate the average score for the entire class and display the average score to the user
average_class = totalscore_class / (num_students * num_tests)
print()
print("Average score for all students is: ", format(average_class, ".2f"))
