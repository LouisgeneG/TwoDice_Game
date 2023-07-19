"""
Author  : Louisgene  
Date    : 7/18/2023
Program : GUI_template.py

GUI-based version of the Two Dice game wich compares random  numbers
and provides the game's outcome.

"""

from breezypythongui import EasyFrame
import tkinter as tk
import random
from tkinter.font import Font
# Other imports go here

# Class header (application name will change project to project)
class TwoDiceGui(EasyFrame):
    # Definition of our class constructor method
    def __init__(self):
        #Call to the Easy Frame constrctor method
        EasyFrame.__init__(self, title = "Two Dice Game", width = 340,
         height = 280, resizable = False, background = "seagreen")
        #Add the various components to the window
        self.addLabel(text = "Two Dice Game", row = 0, column = 0,
         columnspan = 2, sticky = "NSEW", background = "seagreen", font = Font(family = "Impact", size = 24))
        self.addLabel(text = "Player's Roll is:", row = 1, column = 0, sticky = "NE", background = "seagreen")
        self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly", sticky = "NW")
        self.addLabel(text = "Computer's Roll is:", row = 2, column = 0, sticky = "NE", background = "seagreen")
        self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, width = 4, state = "readonly", sticky = "NW")
        self.button = self.addButton(text = "Roll Dice", row = 3, column = 0, columnspan = 2, command = self.roll)
        self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2,
         background = "seagreen", foreground = "yellow", font = Font(family = "Georgia", size = 20), sticky = "NSEW")
    
    #Definition of the roll() function
    def roll(self):
        #variables for this function
        playerDie = random.randint(1, 6)
        compDie = random.randint(1, 6)

        #Processing phase
        if playerDie > compDie:
            result = "Congratulation , you win!"
            self.resultArea["foreground"] = "yellow"
        elif playerDie < compDie:
            result = "Sorry, you lost..."
            self.resultArea["foreground"] = "red"
        else:
            result = "We have a tie."
            self.resultArea["foreground"] = "White"

        # Output phase
        self.playerRoll.setNumber(playerDie)
        self.computerRoll.setNumber(compDie)
        self.resultArea["text"] = result
    

class CenterScreenGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Centered Window")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates for the window
        x = (screen_width // 2) - (500 // 2)  # Center horizontally
        y = (screen_height // 2) - (300 // 2)  # Center vertically

        # Set the window size and position
        self.root.geometry(f"500x300+{x}+{y}")

# Global definition of the main() method
def main():
    # instantiate an object from the class into mainloop()
    TwoDiceGui().mainloop()

# Create an instance of Tkinter root window
root = tk.Tk()
# Create an instance of the CenterScreenGui class
app = CenterScreenGui(root)

# Global call to main() for program entry
if __name__ == '__main__':
    main()