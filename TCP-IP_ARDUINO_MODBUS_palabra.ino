

#include <SPI.h>
#include <Ethernet.h>

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

byte mac[] = {
  0xDE, 0xAA, 0xBE, 0xEF, 0xFE, 0xAA
};
IPAddress ip(192, 168, 2, 137);
EthernetServer ethServer(1003);
ModbusTCPServer modbusTCPServer;

unsigned long  HodingResult, ok ;
unsigned long a0;
int ledPin = 10; 
int duty;

unsigned long a1;
int ledPin2 = 12; 
int duty2;



int in_1 = 22;
int in_2 = 23;
int in_3 = 24;
int in_4 = 25;
int in_5 = 26;
int in_6 = 27;
int in_7 = 28;
int in_8 = 29;


int out_1 = 38;
int out_2 = 39;
int out_3 = 40;
int out_4 = 41;
int out_5 = 42;
int out_6 = 43;
int out_7 = 44;
int out_8 = 45;

byte myByte = 0;


void setup() {

 
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
 
  Ethernet.begin(mac, ip);
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }
  ethServer.begin();

  if (!modbusTCPServer.begin()) {
    Serial.println("Failed to start Modbus TCP Server!");
    while (1);
  }

  

   pinMode(in_1, INPUT);//INPUT 0
   pinMode(in_2, INPUT);//INPUT 1
   pinMode(in_3, INPUT);//INPUT 2
   pinMode(in_4, INPUT);//INPUT 3
   pinMode(in_5, INPUT);//INPUT 4
   pinMode(in_6, INPUT);//INPUT 5
   pinMode(in_7, INPUT);//INPUT 6
   pinMode(in_8, INPUT);//INPUT 7


   pinMode(out_1, OUTPUT);//OUTPUT 0
   pinMode(out_2, OUTPUT);//OUTPUT 1
   pinMode(out_3, OUTPUT);//OUTPUT 2
   pinMode(out_4, OUTPUT);//OUTPUT 3
   pinMode(out_5, OUTPUT);//OUTPUT 4
   pinMode(out_6, OUTPUT);//OUTPUT 5
   pinMode(out_7, OUTPUT);//OUTPUT 6
   
   pinMode(13, OUTPUT);//OUTPUT 7
   pinMode(out_8, OUTPUT);//OUTPUT 7


   digitalWrite(out_1, HIGH);
   digitalWrite(out_2, HIGH);
   digitalWrite(out_3, HIGH);
   digitalWrite(out_4, HIGH);
   digitalWrite(out_5, HIGH);
   digitalWrite(out_6, HIGH);
   digitalWrite(out_7, HIGH);
   digitalWrite(out_8, HIGH);



   pinMode(ledPin, OUTPUT);
  
   digitalWrite(13, HIGH);
   

      
 modbusTCPServer.configureCoils(0x000,37);
 
   
 modbusTCPServer.configureDiscreteInputs(0x016, 22 );
 HodingResult = modbusTCPServer.configureHoldingRegisters(0x6040, 0x072);
  
}

void loop() {
  EthernetClient client = ethServer.available();
  if (client) {
    modbusTCPServer.accept(client);
    while (client.connected()) {
        modbusTCPServer.poll();
        updateLED();
    }
  }
}

void updateLED() {

  
  int coilValue0 = modbusTCPServer.coilRead(0x000);
  int coilValue1 = modbusTCPServer.coilRead(0x001);
  int coilValue2 = modbusTCPServer.coilRead(0x002);
  int coilValue3 = modbusTCPServer.coilRead(0x003);
  int coilValue4 = modbusTCPServer.coilRead(0x004);
  int coilValue5 = modbusTCPServer.coilRead(0x005);
  int coilValue6 = modbusTCPServer.coilRead(0x006);
  int coilValue7 = modbusTCPServer.coilRead(0x007); 

  if (coilValue0) {
    digitalWrite(13, HIGH);
    digitalWrite(out_1, LOW);
    Serial.println("Salida 0- HIGH");
  } else {
    digitalWrite(13, LOW);
    digitalWrite(out_1, HIGH);
    Serial.println("Salida 0- LOW");
  }
//---------------------------------------------//
    if (coilValue1) {
    digitalWrite(out_2, LOW);
    //Serial.println("Salida 1- HIGH");
  } else {
    digitalWrite(out_2, HIGH);
    //bool INPUTD1 = modbusTCPServer.discreteInputWrite(0x016,0);
    //Serial.println("Salida 1- LOW");
  }
//---------------------------------------------//
    if (coilValue2) {
    digitalWrite(out_3, LOW);
    //Serial.println("Salida 2- HIGH");
  } else {
    digitalWrite(out_3, HIGH);
    //Serial.println("Salida 2- LOW");
  }

//---------------------------------------------//
    if (coilValue3) {
    digitalWrite(out_4, LOW);
    //Serial.println("Salida 3- HIGH");
  } else {
    digitalWrite(out_4, HIGH);
    //Serial.println("Salida 3- LOW");
  }  

//---------------------------------------------//
    if (coilValue4) {
    digitalWrite(out_5, LOW);
    //Serial.println("Salida 4- HIGH");
  } else {
    digitalWrite(out_5, HIGH);
    //Serial.println("Salida 4- LOW");
  } 
//---------------------------------------------//
    if (coilValue5) {
    digitalWrite(out_6, LOW);
    //Serial.println("Salida 5- HIGH");
  } else {
    digitalWrite(out_6, HIGH);
    //Serial.println("Salida 5- LOW");
  }  

//---------------------------------------------//
    if (coilValue6) {
    digitalWrite(out_7, LOW);
    //Serial.println("Salida 6- HIGH");
  } else {
    digitalWrite(out_7, HIGH);
    //Serial.println("Salida 6- LOW");
  }   

//---------------------------------------------//
    if (coilValue7) {
    digitalWrite(out_8, LOW);
    //Serial.println("Salida 7- HIGH");
  } else {
    digitalWrite(out_8, HIGH);
    //Serial.println("Salida 7- LOW");
  }  




  myByte = (0x0000000000000000);

//-------IN 0-----------// 
if (digitalRead(in_1)==HIGH) {
   bool INPUTD1 = modbusTCPServer.discreteInputWrite(0x016,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 0, 1 ) ;
   }
   else{
    bool INPUTD1 = modbusTCPServer.discreteInputWrite(0x016,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 0, 0 ) ;
   }
   //bool INPUTD1 = modbusTCPServer.discreteInputRead(0x016);


//-------IN 1-----------// 
if (digitalRead(in_2)==HIGH) {
   bool INPUTD2 = modbusTCPServer.discreteInputWrite(0x017,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 1, 1 ) ;
   }
   else{
    bool INPUTD2 = modbusTCPServer.discreteInputWrite(0x017,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 1, 0 ) ;
   }
   //bool INPUTD2 = modbusTCPServer.discreteInputRead(0x017);


//-------IN 2-----------// 
if (digitalRead(in_3)==HIGH) {
   bool INPUTD3 = modbusTCPServer.discreteInputWrite(0x018,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 2, 1 ) ;
   }
   else{
    bool INPUTD3 = modbusTCPServer.discreteInputWrite(0x018,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 2, 0 ) ;
   }
   //bool INPUTD3 = modbusTCPServer.discreteInputRead(0x018);


//-------IN 3-----------// 
if (digitalRead(in_4)==HIGH) {
   bool INPUTD4 = modbusTCPServer.discreteInputWrite(0x019,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 3, 1 ) ;
   }
   else{
    bool INPUTD4 = modbusTCPServer.discreteInputWrite(0x019,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 3, 0 ) ;
   }
   //bool INPUTD4 = modbusTCPServer.discreteInputRead(0x019);


//-------IN 4-----------// 
if (digitalRead(in_5)==HIGH) {
   bool INPUTD5 = modbusTCPServer.discreteInputWrite(0x020,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 4, 1 ) ;
   }
   else{
    bool INPUTD5 = modbusTCPServer.discreteInputWrite(0x020,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 4, 0 ) ;
   }
   //bool INPUTD5 = modbusTCPServer.discreteInputRead(0x020);



//-------IN 5-----------// 
if (digitalRead(in_6)==HIGH) {
   bool INPUTD6 = modbusTCPServer.discreteInputWrite(0x021,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 5, 1 ) ;
   }
   else{
    bool INPUTD6 = modbusTCPServer.discreteInputWrite(0x021,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 5, 0 ) ;
   }
  // bool INPUTD6 = modbusTCPServer.discreteInputRead(0x021);      


//-------IN 6-----------// 
if (digitalRead(in_7)==HIGH) {
   bool INPUTD7 = modbusTCPServer.discreteInputWrite(0x022,0);
   //Serial.println("I/O ON");
   bitWrite ( myByte, 6, 1 ) ;
   }
   else{
    bool INPUTD7 = modbusTCPServer.discreteInputWrite(0x022,1);
    //Serial.println(" I/O OFF");
    bitWrite ( myByte, 6, 0 ) ;
   }
  // bool INPUTD7 = modbusTCPServer.discreteInputRead(0x022); 


//-------IN 7-----------// 
if (digitalRead(in_8)==HIGH) {
   bool INPUTD8 = modbusTCPServer.discreteInputWrite(0x023,0);
   //Serial.println("I/O 8 ON");
   bitWrite ( myByte, 7, 1 ) ;
   }
   else{
    bool INPUTD8 = modbusTCPServer.discreteInputWrite(0x023,1);
   bitWrite ( myByte, 7, 0 ) ;
   }
   //bool INPUTD8 = modbusTCPServer.discreteInputRead(0x023); 
   //uint16_t bit_data = 0x111111111111111+string(bit_0);



    
   
   



    modbusTCPServer.holdingRegisterWrite(0B0110000001000000, myByte);
                                         
/*
   
  a0 = modbusTCPServer.holdingRegisterRead(0x032); 
  unsigned long J1 = (a0); 
  duty = map(J1, 0, 100, 0, 255); // mapeo el valor de la lectura al rango 0-255
  analogWrite(ledPin, duty);


  a1 = modbusTCPServer.holdingRegisterRead(0x033); 
  unsigned long J2 = (a1); 
  duty2 = map(J2, 0, 100, 0, 255); // mapeo el valor de la lectura al rango 0-255
  analogWrite(ledPin2, duty2);
*/

  
  //Serial.println(J1);
   
a1 = modbusTCPServer.holdingRegisterRead(0x6040);
//Serial.println(a1);

}
                  
