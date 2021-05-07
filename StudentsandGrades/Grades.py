"""
Ask yourself these questions.  How many students will be added to the list?  
How will the program know? What does the program need to know for each student?  
How will the program keep track of the students?  
How will the program display the students after all of them are added?
"""

courses = {"1": "Math", "2": "Science", "3": "History"}

def studentgrades(): #creates the function and defines what it's called
    students = [] # created an empty list (indicated a list by the []) named students
    studentamt = input("How many students do you have?") # asks for a response by input(), everything with "" aroudn it will print. We then set the value of the response to studentamt
    for i in range(int(studentamt)): # for i (where i distinguishes the amount of items within the value's range), int() converts the input value from a string to an integer, studentamt is the input value which has become our range for i. In this case, i will loop through the indented code block following it based off of the studentamt
        name = input("Students name: ") # asks for a response by input() and we set the input response to the variable 'name'
        while name == "": # while loop stating if the variable 'name' equals an empty string (input() always returns the value as a string), then execute the indented code block following
            print("Input a name") # prints out value in the bracketed ""
            name = input("Students name: ") # won't return to line 14 so we must ask the input() again, if we didn't put this line here, it would move onto the next line because the loop was accomplished. Must ask again to get a value that isn't an empty string (any input basically)
        grade = input("Students grade: ") # set the input value to variable grade
        while not grade.isdigit(): # set loop that while the input value is anything but an integer, will execute indented code block below. isdigit() check to see if the value is True or False as an integer
            print("Invalid grade") # prints Invalid grade
            grade = input("Students grade: ") # set input to variable grade
        course = input("Select a course: 1 - Math, 2 - Science, 3 - History: ") # asks for an input and set the input 
        while course not in courses: # the input labeled as course, if input value is not a value in courses (in this case courses is a dictionary, so course is being set equal to the keys within the dictionary)
            print("Invalid course") # prints Invalid course
            course = input("Select a course: 1 - Math, 2 - Science, 3 - History: ") # sets the input to variable course
        student = {"Name": name, "Grade": grade, "Course": courses[course]} # initialized a dictionary and set it equal to student. Gave keys within dictionary and assigned the appropriate variable to it's proper key
        students.append(student) # takes the newly made dictionary named student and adds (appends) it to the list labeled students
    print(students) # prints the list students (the list of dictionaries and all the above basically)

studentgrades() # calls to perform the function named studentgrades