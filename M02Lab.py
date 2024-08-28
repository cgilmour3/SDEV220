'''
Name: Cameron Gilmour
filename: M02Lab.py
Description: This app will accept student names and GPA's
and determine if the student qualifies for Deans list or Honor Roll.
'''
#instantiating a blank last name
lastName = " "
#checking for escape characters
while lastName != "ZZZ":
    lastName =  input("Enter your last name: ")
    #if escape characters are entered, exit program
    if lastName == "ZZZ":
        break
    firstName = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))
    if gpa >=3.5:
        print(f"Congratulations, {firstName} {lastName} has made the Dean's List!")
        #program exits 
    if gpa >= 3.25:
        print(f"Congratulations, {firstName} {lastName} has made honor roll!")
        break
    elif gpa <3.25:
        break
    