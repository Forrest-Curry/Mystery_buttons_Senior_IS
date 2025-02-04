import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

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

#Backend logical objects
lights = [0,0,0,0]
buttons =[[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,1,1,1,]]
winCondition = [1,1,1,1]

def endGame():
    main.destroy()

def CheckWin():
    if lights == winCondition: 
        #messagebox.showinfo(title='Message', message='Game Complette')
        tk.Label(main, text="YOU WIN", font=('DIN Condensed', 50)).place(relx = 0.5, rely = 0.3, anchor = 'center')

def LEDImageChange(arry):
    for i in range(len(arry)):
        if arry[i] == 0:
            tk.Label(LEDframe, image=imgLEDoff_tk).grid(row=0,column=i)

        else:
            tk.Label(LEDframe, image=imgLEDon_tk).grid(row=0,column=i)
    LEDframe.pack(padx=5,pady=5)

def buttonImgSetUp():
    button0 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(0))
    button0.grid(row=0,column=0,sticky=tk.E + tk.W)
    
    button1 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(1))
    button1.grid(row=0,column=1,sticky=tk.E + tk.W)

    button2 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(2))
    button2.grid(row=0,column=2,sticky=tk.E + tk.W)

    button3 = tk.Button(buttonFrame, image=imgButton_tk, command=lambda: buttonImgPress(3))
    button3.grid(row=0,column=3,sticky=tk.E + tk.W)

    buttonFrame.pack(padx=10,pady=10)

    endButton = tk.Button(main, text='QUIT', font=('DIN Condensed', 20), command=endGame)
    endButton.pack(padx=10,pady=10)


def buttonImgPress(buttonNum):
    lightArray= buttonPress(buttonNum)
    LEDImageChange(lightArray)
    CheckWin()





#computes what will happen to the lights when a button is pressed
def buttonPress(num):
    for i in range(len(lights)):
        # ^ is XOR operator to see if a light is turned on or off (1 or 0)
        lights[i] = lights[i] ^ buttons[num][i]
    return lights
    

#randomizes the starting point for the lights ensuring that they are not all 0 
def randomLights(list):
    #creates array of all 1
    null = []
    for i in range(len(list)):
        null.append(1)

    #fills list with either 1 or 0 
    for i in range(len(list)):
        list[i] = random.randint(0,1)
    
    #checks for list of all 0s
    if null == list:
        randomLights(list)
    else:
        return list

def randomButton(list):
    pass

def gameLoop():

    randomLights(lights)
    LEDImageChange(lights)
    buttonImgSetUp()
    main.mainloop()

gameLoop()
