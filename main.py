import random
from datetime import datetime
import tkinter as tk
import numpy as np
from tkinter import messagebox
from PIL import Image, ImageTk

#Randomizes seed for more vaiation in light and button initalization
random.seed(datetime.now().timestamp())

#GUI objects 
main = tk.Tk()
main.geometry('1000x500')
main.title('Game With GUI')

LEDframe = tk.Frame(main)
LEDframe.rowconfigure(0,weight=1)

imgLEDoff = Image.open('imgLEDoff.png')
imgLEDoff_tk = ImageTk.PhotoImage(imgLEDoff)

imgLEDon = Image.open('imgLEDon.png')
imgLEDon_tk = ImageTk.PhotoImage(imgLEDon)

buttonFrame = tk.Frame(main)
buttonFrame.rowconfigure(0,weight=1)

imgButton = Image.open('pushButton.png')
imgButton_tk = ImageTk.PhotoImage(imgButton)

#Backend logical objects used as global variables
lights = [0,0,0,0]
buttons =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0,]]
winCondition = [1,1,1,1]

#GAME RUNTIME FUNCTIONS

#calls chain of fucntons to happen when a button is pressed
def buttonImgPress(buttonNum):
    #computes change of lights based on specific button
    computeGameLogic(buttonNum)
    #changes lights to match new lights Array global variable
    LEDImageChange()
    #checks if win condition met
    CheckWin()

#computes what will happen to the lights when a button is pressed
#Changes lights array as Global variable 
def computeGameLogic(num):
    global lights
    for i in range(len(lights)):
        # ^ is XOR operator to see if a light is turned on or off (1 or 0)
        lights[i] = lights[i] ^ buttons[num][i]
    return 0

#adjusts GUI LED's to match internal array representation
#replaces and covers up previous lights in LEDframe each time lights change
def LEDImageChange():
    for i in range(len(lights)):
        if lights[i] == 0:
            tk.Label(LEDframe, image=imgLEDoff_tk).grid(row=0,column=i)

        else:
            tk.Label(LEDframe, image=imgLEDon_tk).grid(row=0,column=i)
    LEDframe.pack(padx=5,pady=5)

#Checks win condition, adds label in center of display if win condition is met
def CheckWin():
    if lights == winCondition: 
        tk.Label(main, text="YOU WIN", font=('DIN Condensed', 50)).place(relx = 0.5, rely = 0.3, anchor = 'center')

#End game function acsessed by 'Quit' button
def endGame():
    main.destroy()


#INITALIZATION FUNCTIONS

#Initalizes and starts the GUI game loop
def gameLoop():
    #Randimizes the initalization of lights as Global variable
    randomLights()
    #Randomizes the initalization of the buttons
    randomButton()
    print('buttons: ', buttons)
    #Sets GUI lights to match on/off state of internal representation
    LEDImageChange()
    #initalizes the buttons in GUI
    buttonImgSetUp()
    #Starts the game function in GUT
    main.mainloop()

#randomizes the starting point for the lights ensuring that they are not all 0 
#using lights as global variable
def randomLights():
    #creates array of all 1
    global lights

    null = []
    for i in range(len(lights)):
        null.append(1)

    #fills list with either 1 or 0 
    for i in range(len(lights)):
        lights[i] = random.randint(0,1)
    
    #checks for list of all 0s
    if null == lights:
        randomLights(lights)
    else:
        return 0

#Randomizes intialization of buttons as global variable
def randomButton():
    global buttons
    npList = np.array(buttons) #convert button array to numpy arry

    for i in range(4):
        for j in range(4):
            npList[i][j] = random.randint(0,1) # fill arry with random 0 or 1s
    
    #check if linearly independent, refill array untill linearly independent
    rank = np.linalg.matrix_rank(npList)
    while (rank != npList.shape[1]): 
        print('Linearly Dependent')
        for i in range(4):
            for j in range(4):
                npList[i][j] = random.randint(0,1)

        rank = np.linalg.matrix_rank(npList)
        
    print('Linearly Independent')

    #convert back to standerd array and reasign to change input array
    buttons = npList.tolist()
    return 0

#Sets up button GUI
def buttonImgSetUp():
    #command=lambda: buttonImgPress() allows number associated with 
    # button to be passed to function with button press
    button0 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(0))
    #palces button into grid
    button0.grid(row=0,column=0,sticky=tk.E + tk.W)
    
    button1 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(1))
    button1.grid(row=0,column=1,sticky=tk.E + tk.W)

    button2 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(2))
    button2.grid(row=0,column=2,sticky=tk.E + tk.W)

    button3 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(3))
    button3.grid(row=0,column=3,sticky=tk.E + tk.W)

    #packs button frame into window
    buttonFrame.pack(padx=10,pady=10)

    #button to exit game 
    endButton = tk.Button(main, text='QUIT', font=('DIN Condensed', 20), command=endGame)
    endButton.pack(padx=10,pady=10)


#MAIN block of code 
#call gameLoop() to start game
gameLoop()
