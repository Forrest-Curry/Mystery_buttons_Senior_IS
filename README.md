# Mystery Buttons Game
This GitHub repository contains the software materials and images of the hardware materials that coincide with my 2025 Senior Independent Study project at the College of Wooster. The project creates the same puzzle game in three implementations: software, an Arduino circuit, and a raw circuit with no processor. 

## Software 
Files: `SoftwareGame.py`, `imgLEDoff.png`, `imgLEDon.png`, `pushButton.png`
The software implementation is written in Python and uses the following modules and libraries: random, datetime, Tkinter, Numpy,  and Image and ImageTk from Pillow. 
The game can be run and played by executing the SoftwareGame.py file.

## Arduino circuit
File: `ArduinoSoftware.ino`
The Arduino circuit has two parts, the software and the physical circuit. The software will present errors unless opened in the [Arduino IDE](https://www.arduino.cc/en/software). 
The pin setup for the physical board is as follows: 
LED outputs in pins: 3,4,5,6
Button inputs in pins: 8,9,10,11 

The circuit implementation can be seen in the following image: 
![Image](https://github.com/user-attachments/assets/906cfe16-5f3b-4fd5-a860-3b51d0083c7f)

## Raw Circuit
The raw circuit contains only hardware components. An image of the physical implementation and an image of the abstract circuit diagram are shown below. 

<img width="1049" alt="Picture of circuit implementation" src="https://github.com/user-attachments/assets/05ac2434-e8a7-4190-a0ff-33e9e4b7ea7e" />

<img width="1266" alt="Circuit Diagram" src="https://github.com/user-attachments/assets/0797e9f6-6bb2-4bec-9b89-1c01baa6c828" />
