#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    print('welcome to the geometric shape area calculator')
    # User Options
    Circle = 1
    Rectangle = 2
    Triangle = 3
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
    print('Circle = 1' + ' ' + 'Rectangle = 2' + ' ' + 'Triangle = 3' )
    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'.
    choice = input("Select a shape by entering 1, 2, 3")
    print(choice)
    choice = int(choice)
    # TODO: Convert the variable 'choice' to an integer data type.
    
    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.
    print("True" if isinstance(choice, int) else "False")
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle
        radius = input("what is the radius of the cirle?")
        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
        print(radius)
        radius = float(radius)
        # TODO: Convert 'radius' to float.
        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
        area = (circle_pi * radius**2)
        print(area)
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width
        length = input("what is the length of the rectangle?")
        print(length)
        length = float(length)
        width = input("What is the width of the rectangle?")
        print(width)
        width = float(width)
        area = length * width
        print(area)


    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height
     base = input("what is th base length of the triangle?")
     print(base)
     base = float(base)
     height = input("What is the heighth of the triangle?")
     print(height)
     height = float(height)
     area = .5 * base * height
     print(area)

    #  else:
        # TODO:  
    else: print('Invalid choice .')
    
    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 
print("The steps required to do this assignment were to read each of the following instuctuions given in the assignment and have a understanding of the task. ")
print("step 1  was easy using the print statement to print out welcome to the geomentric shape caluclulator")
print("step to required me to make a concadinated list of each coice that the input would eneter")
print("add a input requesest in for the user to make a choice from the list that was given")
print("the next step is to make change data type a integer")
print("after writing the code to change input variable to int. from sting i had to double check to make sure it was using a boolean statement")
print("after that i had to write code designed to check the areas of each shape and usingg the input data from the user using equations")
print("lastly make a else statement to say invalid choice if the user input was anything other than 1,2,or3")

# if __name__ == "__main__": # DO NOT MODIFY
# main() # DO NOT MODIFY
