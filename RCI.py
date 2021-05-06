#ROBOT CONTROL INTERFACE------------------------------------------------------
#Communicate over serial with Control Scripts to tell motors to move----------
#as well as how to move (path planning and INVKIN)----------------------------

import numpy
import math
import serial
import tkinter as tk

#INCOMMING DATA FROM SENSORS
encoder1 = ("some serial data measurement")
encoder2 = ("some serial data measurement")
encoder3 = ("some serial data measurement")
encoder4 = ("some serial data measurement")
encoder5 = ("some serial data measurement")
encoder6 = ("some serial data measurement")

#Measure velocity by checking for rate of change of encoder position
#as well as known facts about physical system to convert pulse rate 
# into an angular velocity, then check how quickly the angular 
# velocity is changing to get angular acceleration

#INV KINEMATICS
thetaj1 = ("Mathematical Equation from General Transformation Matrix")
thetaj2 = ("Mathematical Equation from General Transformation Matrix")
thetaj3 = ("Mathematical Equation from General Transformation Matrix")
thetaj4 = ("Mathematical Equation from General Transformation Matrix")
thetaj5 = ("Mathematical Equation from General Transformation Matrix")
thetaj6 = ("Mathematical Equation from General Transformation Matrix")

#END EFFECTOR CONTROL
ee_status = ("Result of listening for close command")#boolean (closed or open)

#PATH PLANNING CODE
#For now it should just perform cubic regression on the start and end points--
#with some basic linear points bridging between-------------------------------

traj = ("Some function that gives a list of points from current to desired")


#UI Stays at the bottom of the program, everything it needs must be made------
#first right? ----------------------------------------------------------------

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text ='Click this to Quit', 
        command = self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('RCI v' + "0.00")
app.mainloop()    

#ihopethisworksnow