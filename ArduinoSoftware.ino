//Initalize component pins, static
const int LED1pin = 3;
const int LED2pin = 4;
const int LED3pin = 5;
const int LED4pin = 6;
const int button1Pin = 8;
const int button2Pin = 9;
const int button3Pin = 10;
const int button4Pin = 11;

//Initalize changing variables
int LED1state = LOW;
int LED2state = LOW;
int LED3state = LOW;
int LED4state = LOW;
int button1LastState = LOW;
int button2LastState = LOW;
int button3LastState = LOW;
int button4LastState = LOW;
int button1CurrentState;
int button2CurrentState;
int button3CurrentState;
int button4CurrentState;

//Timer used to debounce buttons
unsigned long lastDebounceTime  = 0; //previous toggle time
unsigned long debounceDelay = 80; //timing for debounce, increase if light flikers 

void setup() {
  //Creates Random seed based on nosie from unused pin
  randomSeed(analogRead(A0)); 
  
  //randomize the intialization of LEDs
  //Ensured that not all lights are in the same on/off state 
  while ((LED1state == LED2state)&&(LED2state == LED3state)&&(LED3state == LED4state)){
    LED1state=random(0,2); //Randomly asigns value to LED state of eather HIGH = 1, or LOW = 0
    LED2state=random(0,2); //random(0,2) is [0,2), 0 inclusive, 2 exclusive
    LED3state=random(0,2);
    LED4state=random(0,2);
  }

  //define pin inputs and outputs
  pinMode(LED1pin, OUTPUT);
  pinMode(LED2pin, OUTPUT);
  pinMode(LED3pin, OUTPUT);
  pinMode(LED4pin, OUTPUT);
  pinMode(button1Pin, INPUT);
  pinMode(button2Pin, INPUT);
  pinMode(button3Pin, INPUT);
  pinMode(button4Pin, INPUT);

  //Write inital state of LEDs based on random initalization
  digitalWrite(LED1pin, LED1state);
  digitalWrite(LED2pin, LED2state);
  digitalWrite(LED3pin, LED3state);
  digitalWrite(LED4pin, LED4state);

  //initalize current state of button
  button1CurrentState = digitalRead(button1Pin);
  button2CurrentState = digitalRead(button2Pin);
  button3CurrentState = digitalRead(button3Pin);
  button4CurrentState = digitalRead(button4Pin);
}


void loop() {
  //Read in any input from the buttons
  int button1Read = digitalRead(button1Pin);
  int button2Read = digitalRead(button2Pin);
  int button3Read = digitalRead(button3Pin);
  int button4Read = digitalRead(button4Pin);
  
  //Chceks for lass button press from smae button to account for debounce
  if (button1Read != button1LastState){
    lastDebounceTime = millis();
  }

  if (button2Read != button2LastState){
    lastDebounceTime = millis();
  }

  if (button3Read != button3LastState){
    lastDebounceTime = millis();
  }

  if (button4Read != button4LastState){
    lastDebounceTime = millis();
  }
  
  //if button press is outside debounceDelay proced with puzzle logic
  if ((millis() - lastDebounceTime)> debounceDelay){

    //Button 1 controlls one light
    if (button1Read != button1CurrentState){
      button1CurrentState = button1Read;

      //inverts LED state if associated button is pressed
      if (button1CurrentState == HIGH){
        LED1state = !LED1state;
      }
    }

    //button 2 controlls two lights
    if (button2Read != button2CurrentState){
      button2CurrentState = button2Read;

      //inverts LED state if associated button is pressed
      if (button2CurrentState == HIGH){
        LED1state = !LED1state;
        LED2state = !LED2state;
      }
    }

    //button 3 controlls 3 lights
    if (button3Read != button3CurrentState){
      button3CurrentState = button3Read;

      //inverts LED state if associated button is pressed
      if (button3CurrentState == HIGH){
        LED1state = !LED1state;
        LED2state = !LED2state;
        LED3state = !LED3state;
      }
    }
    //button 4 controlls 4 lights
    if (button4Read != button4CurrentState){
      button4CurrentState = button4Read;

      //inverts LED state if associated button is pressed
      if (button4CurrentState == HIGH){
        LED1state = !LED1state;
        LED2state = !LED2state;
        LED3state = !LED3state;
        LED4state = !LED4state;
      }
    }
  }
  //assign LEDs to new state
  digitalWrite(LED1pin, LED1state);
  digitalWrite(LED2pin, LED2state);
  digitalWrite(LED3pin, LED3state);
  digitalWrite(LED4pin, LED4state);
  
  //reasign the button state to reset debounce
  button1LastState = button1Read;
  button2LastState = button2Read;
  button3LastState = button3Read;
  button4LastState = button4Read;

}
