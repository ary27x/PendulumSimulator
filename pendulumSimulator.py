from tkinter import *
import time
import sys
import math
import os
os.system("cls")



planet = int(input("Choose the planet to simulate the pendulum on : \n1)Earth (9.807 m/s^2) \n2)Moon (1.625 m/s^2) \n3)Mars (3.7 m/s^2) \n4)Jupiter (24.5 m/s^2) \n"))
planetString = ""

if (planet == 1):
	gravity = 9.807
	planetString = "Earth"
elif (planet == 2):
	gravity = 1.625
	planetString = "Moon"
elif (planet == 3):
	gravity = 3.7
	planetString = "Mars"
elif (planet == 4):
	gravity = 24.5
	planetString = "Jupiter"
else:		
	print("Please enter a valid choice ")
	sys.exit()	

theta = int(input("\nEnter the value of theta : (between 0 and 90) : "))
if (theta < 0 or theta > 90):
	print("The value of theta should be in between 0 and 90")
	sys.exit()
drag = float(input("Enter the drag factor: (Between 0 and 1 , 0 for ideal case) : "))
if (drag < 0 and drag > 1):
	print("Please enter the correct value for the drag")
	sys.exit()
if (drag == 0):
	print("~ IDEAL CASE ~ (No air friction) \n")
dragSave = drag
drag = drag /3


print("Starting the bob from the position : " , theta , "degrees")
print("Applying gravity of : " , gravity , "m/s^2")






simulator = Tk()
simulator.title("Pendulum Simulator")
simulator.geometry("1000x800")
canvas = Canvas(simulator, bg="black",width=(1000),height=(800))

canvas.pack()
	


change = -(gravity / 1.5) # this can be changed
frameRate = 15





# System Constants
length = 300
baseTheta = theta
baseX = 500
baseY = 0
bobRadius = 20
endMessage = True


endX = baseX + (length * round((math.sin(math.radians(theta)))))
endY = length * round((math.cos(math.radians(theta))))

def updatePosition():
	
	global theta , endX , endY , baseX , baseY , change , baseTheta , simulator , endMessage , startTime
	if (baseTheta <= 0):
		if (endMessage):
			print("Value of theta :  0.00000000000000000")
			print("\nThe pendulum has stopped !!! ")
			
			endMessage = False	
		return
	theta = theta + change
	baseTheta = baseTheta - drag
	if (abs(theta) < 0.001):
		displayTheta = 0.000000001
	else:
		displayTheta = abs(theta)
	print("Value of theta : " , displayTheta , end = "\r")
	
	if (theta < -baseTheta or theta > baseTheta):	
		
		theta = baseTheta * (change //abs(change)) 
		change = change * (-1)
		
	endX = baseX + (length * (math.sin(math.radians(theta))))
	endY = length * (math.cos(math.radians(theta)))

	canvas.coords(string , baseX , baseY,endX,endY)
	canvas.coords(bob, endX  - bobRadius, endY  - bobRadius, endX  + bobRadius, endY  + bobRadius)
	simulator.update()
	simulator.after(frameRate , updatePosition)
	

canvas.create_rectangle(0,0,1000,10 , fill = "saddle brown")
string = canvas.create_line(baseX ,baseY,endX,endY, fill="white", width=1)
bob = canvas.create_oval(endX  - bobRadius, endY  - bobRadius, endX  + bobRadius, endY  + bobRadius , fill = "red")
dragDisplay = canvas.create_text(485 , 450 , text = "Drag Factor : " + str(dragSave) , fill = "white" , font = ("Arial" , 20))
gravityDisplay = canvas.create_text(485 , 480 , text = "Gravity : " + str(gravity) + " (" + planetString + ")" , fill ="white" , font = ("Arial" , 20))
updatePosition()
simulator.mainloop()
