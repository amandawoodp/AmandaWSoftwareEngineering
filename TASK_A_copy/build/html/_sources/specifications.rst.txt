Specifications
==============

It is important to clarify some aspects of our software for better understanding. QuickFit is an application that allows users to create personalized workout routines tailored to their available space and time. 

The software is built around a database of exercises, each with specific attributes such as priority, identification number, required time, and necessary equipment. Using Python, a code is developed to filter these exercises based on the equipment and time provided by the user as input.

The program features three interface windows, developed using the PyQt6 visual programming framework:
1. The first window serves as a welcome screen.
2. The second collects user inputs.
3. The third displays images of the exercises included in the routine.

Requirements
============

- The program must be run on a computer that has Python and PyQt6 installed.
- The program will filter the exercises depending on the implements and time the user specifies.
- Users can select multiple options when asked about the implements they have.
- Users can only select one time option when asked how much time they have.
- The interface will be simple and intuitive, making interactions friendly for any type of user.
- The program should recommend a routine and filter the exercises in less than 30 seconds.
- The program will need user input.

System Interfaces
=================

As mentioned before, the software has three interface windows:

1. **Welcome Screen (First Window):**
   - Works independently.
   - Displays a friendly welcome to the users.

2. **User Input Collection (Second Window):**
   - Collects the user's inputs: time and implements.
   - Provides buttons that allow navigation to the third window.

3. **Exercise Display (Third Window):**
   - Displays images of the exercises included in the routine.
   - Relies on the input from the second window to generate and show the workout.
   - Includes a button to return to the first window.

Navigation between Windows
--------------------------

- From the **second window**, the user can navigate to the third window after specifying inputs.
- From the **third window**, there is a button that allows the user to return to the first window.
