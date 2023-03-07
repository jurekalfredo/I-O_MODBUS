#! /usr/bin/python
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------
# Biblotecas Python
#-----------------------------------------------------------------------

     
import threading
import time
from tkinter import messagebox
from distutils.dir_util import copy_tree
import asyncio
import  tkinter.filedialog
from tkinter import ttk
from tkinter import *        
import tkinter as tk
from pyModbusTCP.client import ModbusClient
import signal
from PIL import Image as Img
from PIL import ImageTk

from serializacion2 import*
from DICCIONARIO import*

global comparo
comparo =[0]
COLORFONDO = 'white'
TIM_1 = 0.01
#-----------------------------------------------------------------------
# Class Software
#-----------------------------------------------------------------------
class Soft(threading.Thread):#object):
      def __init__(self):#, **kwargs):
            self.loop = asyncio.get_event_loop()
            threading.Thread.__init__(self)
            self.start()
            ### SALIDAS DE MODULO FISICO
            self.salida_0 = False
            self.salida_1 = False
            self.salida_2 = False
            self.salida_3 = False
            self.OUT_1 = False
            self.OUT_2 = False
            self.OUT_3 = False
            self.OUT_4 = False
            self.OUT_5 = False
            self.OUT_6 = False
            self.OUT_7 = False
            self.OUT_8 = False
            self.ventana_edit = False

            self.root = tk.Tk()       
            self.root.image = tk.PhotoImage(file='Marco_blanco.png')
            self.label = tk.Label(self.root, image=self.root.image)
            self.root.geometry("+0+0")

            #self.root.wm_attributes('-type', 'splash')
            self.frame_1=Frame(self.root, width=500, height=380, relief = 'ridge',bg=COLORFONDO)
            self.frame_1.place(x=1, y=30)

            self.frame_2=Frame(self.root, width=500, height=380, relief = 'ridge',bg=COLORFONDO)
            self.frame_2.place(x=1, y=420)

            #self.root.wm_attributes('-type', 'splash')
            self.frame_3=Frame(self.root, width=500, height=380, relief = 'ridge',bg=COLORFONDO)
            self.frame_3.place(x=1, y=100000)
            #===============================================================================
            # Menu Barra
            #===============================================================================
            menubarra = Menu(self.root)
            self.menuprograma = Menu(menubarra, tearoff=0)
            self.menuprograma.add_command(label="Cerrar", command=self.cerrar)
            menubarra.add_cascade(label="Programa", menu=self.menuprograma)
            self.root.config(menu=menubarra)
            

            self.root.runTrue = 0
            self.root.FWDTrue = 0
            
            self.STATUS_IN = 'I/O OFF'
            self.dat_analog_1 = Label(self.frame_3, font=("helvetica", 12, "bold"),text = " CORRIENTE %", width=15, bg='white', relief = 'ridge')
            self.dat_analog_1.place(x=5, y=300)
        
            self.analog_1 =Entry(self.frame_3,font=("Lucida Console", 10, "bold"), width=9,relief = 'flat', bg='bisque',justify='left')#.format(N53)
            self.analog_1.place(x=150, y=300)

            self.dat_analog_2 = Label(self.frame_3, font=("helvetica", 12, "bold"),text = " TENSION % ", width=15, bg='white', relief = 'ridge')
            self.dat_analog_2.place(x=5, y=340)
        
            self.analog_2 =Entry(self.frame_3,font=("Lucida Console", 10, "bold"), width=9,relief = 'flat', bg='bisque',justify='left')#.format(N53)
            self.analog_2.place(x=150, y=340)
     
            self.analog_1.delete(0, 'end')
            self.analog_1.insert(0,str("1"))

            self.analog_2.delete(0, 'end')
            self.analog_2.insert(0,str("1"))
            
            #self.root.wm_attributes('-type', 'splash')
            self.frame_4=Frame(self.root, width=500, height=380, relief = 'ridge',bg=COLORFONDO)
            self.frame_4.place(x=1, y=1000)
        
            self.open_1()
      #-----------------------------------------------------------------------
      # STATUS IN
      #----------------------------------------------------------------------- 
      def UpdateStatus_in(self,set_status_in=None):
            try:
                  if set_status_in is not None:
                        self.STATUS_IN = set_status_in
                  #----------------
                  # IN_0
                  #----------------
      
                  if self.STATUS_IN == '1 I/O OFF':
                        self.li_1.delete('1.0',END)
                        self.li_1['bg']="red"
                        self.li_1_['bg']="red"
                        self.li.insert(END, str("I/O 1 OFF"))
                        self.salida_0 = False
                        
                  elif self.STATUS_IN == '1 I/O ON':
                        self.li_1.delete('1.0',END)
                        self.li_1['bg']="green3"
                        self.li_1_['bg']="green3"
                        self.li_1.insert(END, str("I/O 1 ON"))
                        self.salida_0 = True
                  #----------------
                  # IN_1
                  #----------------      
                  elif self.STATUS_IN == '2 I/O OFF':
                        self.li_2.delete('1.0',END)
                        self.li_2['bg']="red"
                        self.li_2.insert(END, str("I/O 2 OFF"))
                        self.li_2_['bg']="red"
                        self.salida_1 = False
                        
                  elif self.STATUS_IN == '2 I/O ON':
                        self.li_2.delete('1.0',END)
                        self.li_2['bg']="green3"
                        self.li_2.insert(END, str("I/O 2 ON"))
                        self.li_2_['bg']="green3"
                        self.salida_1 = True
                        
                  #----------------
                  # IN_2
                  #----------------      
                  elif self.STATUS_IN == '3 I/O OFF':
                        self.li_3.delete('1.0',END)
                        self.li_3['bg']="red"
                        self.li_3.insert(END, str("I/O 3 OFF"))
                        self.li_3_['bg']="red"
                        self.salida_2 = False
                        
                  elif self.STATUS_IN == '3 I/O ON':
                        self.li_3.delete('1.0',END)
                        self.li_3['bg']="green3"
                        self.li_3.insert(END, str("I/O 3 ON"))
                        self.li_3_['bg']="green3"
                        self.salida_2 = True
                        
                  #----------------
                  # IN_3
                  #----------------      
                  elif self.STATUS_IN == '4 I/O OFF':
                        self.li_4.delete('1.0',END)
                        self.li_4['bg']="red"
                        self.li_4.insert(END, str("I/O 4 OFF"))
                        self.li_4_['bg']="red"
                        self.salida_3 = False
                        
                  elif self.STATUS_IN == '4 I/O ON':
                        self.li_4.delete('1.0',END)
                        self.li_4['bg']="green3"
                        self.li_4.insert(END, str("I/O 4 ON"))
                        self.li_4_['bg']="green3"
                        self.salida_3 = True
                                          
                  #----------------
                  # IN_4
                  #----------------      
                  elif self.STATUS_IN == '5 I/O OFF':
                        self.li_5.delete('1.0',END)
                        self.li_5['bg']="red"
                        self.li_5.insert(END, str("I/O 5 OFF"))
                        self.li_5_['bg']="red"
                        
                  elif self.STATUS_IN == '5 I/O ON':
                        self.li_5.delete('1.0',END)
                        self.li_5['bg']="green3"
                        self.li_5.insert(END, str("I/O 5 ON"))
                        self.li_5_['bg']="green3"
                        
                  #----------------
                  # IN_5
                  #----------------      
                  elif self.STATUS_IN == '6 I/O OFF':
                        self.li_6.delete('1.0',END)
                        self.li_6['bg']="red"
                        self.li_6.insert(END, str("I/O 6 OFF"))
                        self.li_6_['bg']="red"
                        
                  elif self.STATUS_IN == '6 I/O ON':
                        self.li_6.delete('1.0',END)
                        self.li_6['bg']="green3"
                        self.li_6.insert(END, str("I/O 6 ON"))
                        self.li_6_['bg']="green3"
                        
                  #----------------
                  # IN_6
                  #----------------      
                  elif self.STATUS_IN == '7 I/O OFF':
                        self.li_7.delete('1.0',END)
                        self.li_7['bg']="red"
                        self.li_7.insert(END, str("I/O 7 OFF"))
                        self.li_7_['bg']="red"
                        
                  elif self.STATUS_IN == '7 I/O ON':
                        self.li_7.delete('1.0',END)
                        self.li_7['bg']="green3"
                        self.li_7.insert(END, str("I/O 7 ON"))
                        self.li_7_['bg']="green3"
                        
                  #----------------
                  # IN_7
                  #----------------      
                  elif self.STATUS_IN == '8 I/O OFF':
                        self.li_8.delete('1.0',END)
                        self.li_8['bg']="red"
                        self.li_8.insert(END, str("I/O 8 OFF"))
                        self.li_8_['bg']="red"
                        
                  elif self.STATUS_IN == '8 I/O ON':
                        self.li_8.delete('1.0',END)
                        self.li_8['bg']="green3"
                        self.li_8.insert(END, str("I/O 8 ON"))
                        self.li_8_['bg']="green3"
                  else:
                        None
            except:
                  None
      def run(self):
            async def while_loop():
                  while True:
                        start = time.time()
                        await asyncio.sleep(TIM_1)
                        ss=INPUT_OBJECT.get()#llamo al elemento INPUT_OBJECT, del diccionario y me traigo su valor
                        bit_=bit_in(ss)# lo convierto en una lista 
                        for i in range(16):
                              if(bit_[i]=='1'):
                                    self.UpdateStatus_in(str(i+1)+' I/O ON')
                              else:
                                    self.UpdateStatus_in(str(i+1)+' I/O OFF')     
                  end = time.time()      
                  TIMER = (end - start) 
            self.future = self.loop.create_task(while_loop())
            self.loop.run_until_complete(self.future)


      def cerrar(self):
            self.root.destroy()
            sys.exit()                      
      def open_1(self):
        self.label.pack()

        ''' CONFIGURACION DE ENTRADAS '''
        self._in_o = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 0 ", width=8, bg='white', relief = 'ridge')
        self._in_o.place(x=0, y=40)
        
        self.li=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li.place(x=80,y=40)

        self._in_2 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 1 ", width=8, bg='white', relief = 'ridge')
        self._in_2.place(x=0, y=70)

        self.li_2=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_2.place(x=80,y=70)

        self._in_3 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 2 ", width=8, bg='white', relief = 'ridge')
        self._in_3.place(x=0, y=100)

        self.li_3=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_3.place(x=80,y=100)

        self._in_4 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 3 ", width=8, bg='white', relief = 'ridge')
        self._in_4.place(x=0, y=130)

        self.li_4=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_4.place(x=80,y=130)

        self._in_5 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 4 ", width=8, bg='white', relief = 'ridge')
        self._in_5.place(x=0, y=160)

        self.li_5=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_5.place(x=80,y=160)

        self._in_6 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 5 ", width=8, bg='white', relief = 'ridge')
        self._in_6.place(x=0, y=190)

        self.li_6=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_6.place(x=80,y=190)

        self._in_7 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 6 ", width=8, bg='white', relief = 'ridge')
        self._in_7.place(x=0, y=220)

        self.li_7=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_7.place(x=80,y=220)

        self._in_8 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 7 ", width=8, bg='white', relief = 'ridge')
        self._in_8.place(x=0, y=250)

        self.li_8=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_8.place(x=80,y=250)

        ''' CONFIGURACION DE SALIDAS '''
        
        def BUT_1(event):
              if (self.BUT_OUT1['bg']== 'green2'):
                    self.BUT_OUT1['bg']= 'red'
                    self.OUT_1 = False
              else:
                    self.BUT_OUT1['bg']= 'green2'
                    self.OUT_1 = True
                    
        def BUT_2(event):
              if (self.BUT_OUT2['bg']== 'green2'):
                    self.BUT_OUT2['bg']= 'red'
                    self.OUT_2 = False
              else:
                    self.BUT_OUT2['bg']= 'green2'
                    self.OUT_2 = True
                    
        def BUT_3(event):
              if (self.BUT_OUT3['bg']== 'green2'):
                    self.BUT_OUT3['bg']= 'red'
                    self.OUT_3 = False
              else:
                    self.BUT_OUT3['bg']= 'green2'
                    self.OUT_3 = True
                    
        def BUT_4(event):
              if (self.BUT_OUT4['bg']== 'green2'):
                    self.BUT_OUT4['bg']= 'red'
                    self.OUT_4 = False
              else:
                    self.BUT_OUT4['bg']= 'green2'
                    self.OUT_4 = True
                    
        def BUT_5(event):
              if (self.BUT_OUT5['bg']== 'green2'):
                    self.BUT_OUT5['bg']= 'red'
                    self.OUT_5 = False
              else:
                    self.BUT_OUT5['bg']= 'green2'
                    self.OUT_5 = True
                    
        def BUT_6(event):
              if (self.BUT_OUT6['bg']== 'green2'):
                    self.BUT_OUT6['bg']= 'red'
                    self.OUT_6 = False
              else:
                    self.BUT_OUT6['bg']= 'green2'
                    self.OUT_6 = True
                    
        def BUT_7(event):
              if (self.BUT_OUT7['bg']== 'green2'):
                    self.BUT_OUT7['bg']= 'red'
                    self.OUT_7 = False
              else:
                    self.BUT_OUT7['bg']= 'green2'
                    self.OUT_7 = True
                    
        def BUT_8(event):
              if (self.BUT_OUT8['bg']== 'green2'):
                    self.BUT_OUT8['bg']= 'red'
                    self.OUT_8 = False
              else:
                    self.BUT_OUT8['bg']= 'green2'
                    self.OUT_8 = True

        #-------OUT 1---------#            
        self._out_1 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " ejecuto", height=1, width=5, bg='white', relief = 'ridge')
        self._out_1.place(x=320, y=42)

        self.BUT_OUT1 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT1.place(x=400, y=40)

        self.BUT_OUT1.bind( "<Button>",BUT_1 )
        self.BUT_OUT1['bg']= 'red'
        #-------OUT 2---------#            
        self._out_2 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " start ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_2.place(x=320, y=72)

        self.BUT_OUT2 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT2.place(x=400, y=70)

        self.BUT_OUT2.bind( "<Button>",BUT_2 )
        self.BUT_OUT2['bg']= 'red'
        #-------OUT 3---------#            
        self._out_3 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " man/auto ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_3.place(x=320, y=102)

        self.BUT_OUT3 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT3.place(x=400, y=100)

        self.BUT_OUT3.bind( "<Button>",BUT_3 )
        self.BUT_OUT3['bg']= 'red'
        #-------OUT 4---------#            
        self._out_4 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " paso adelante ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_4.place(x=320, y=132)

        self.BUT_OUT4 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT4.place(x=400, y=130)

        self.BUT_OUT4.bind( "<Button>",BUT_4 )
        self.BUT_OUT4['bg']= 'red'
        #-------OUT 5---------#            
        self._out_5 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " paso atras ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_5.place(x=320, y=162)

        self.BUT_OUT5 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT5.place(x=400, y=160)

        self.BUT_OUT5.bind( "<Button>",BUT_5 )
        self.BUT_OUT5['bg']= 'red'
        #-------OUT 6---------#            
        self._out_6 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 5 ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_6.place(x=320, y=192)

        self.BUT_OUT6 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT6.place(x=400, y=190)

        self.BUT_OUT6.bind( "<Button>",BUT_6 )
        self.BUT_OUT6['bg']= 'red'
        #-------OUT 7---------#            
        self._out_7 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " IN 6 ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_7.place(x=320, y=222)

        self.BUT_OUT7 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT7.place(x=400, y=220)

        self.BUT_OUT7.bind( "<Button>",BUT_7 )
        self.BUT_OUT7['bg']= 'red'
        #-------OUT 8---------#            
        self._out_8 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " reset ", height=1, width=5, bg='white', relief = 'ridge')
        self._out_8.place(x=320, y=252)

        self.BUT_OUT8 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT8.place(x=400, y=250)

        self.BUT_OUT8.bind( "<Button>",BUT_8 )
        self.BUT_OUT8['bg']= 'red'

        self.frame_3.place(x=1, y=0)
        #################################################
        ##########      AGREGADO    #####################
        #################################################

        
        # CONFIGURACION DE ENTRADAS 
        self._in_1 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 0 ", width=16, bg='white', relief = 'ridge')
        self._in_1.place(x=0, y=40)
        
        self.li_1=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_1.place(x=180,y=40)

        self._in_2 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 1 ", width=16, bg='white', relief = 'ridge')
        self._in_2.place(x=0, y=70)

        self.li_2=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_2.place(x=180,y=70)

        self._in_3 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 2 ", width=16, bg='white', relief = 'ridge')
        self._in_3.place(x=0, y=100)

        self.li_3=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_3.place(x=180,y=100)

        self._in_4 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 3 ", width=16, bg='white', relief = 'ridge')
        self._in_4.place(x=0, y=130)

        self.li_4=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_4.place(x=180,y=130)

        self._in_5 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 4 ", width=16, bg='white', relief = 'ridge')
        self._in_5.place(x=0, y=160)

        self.li_5=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_5.place(x=180,y=160)

        self._in_6 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 5 ", width=16, bg='white', relief = 'ridge')
        self._in_6.place(x=0, y=190)

        self.li_6=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_6.place(x=180,y=190)

        self._in_7 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 6 ", width=16, bg='white', relief = 'ridge')
        self._in_7.place(x=0, y=220)

        self.li_7=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_7.place(x=180,y=220)

        self._in_8 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 7 ", width=16, bg='white', relief = 'ridge')
        self._in_8.place(x=0, y=250)

        self.li_8=Text(self.frame_3,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_8.place(x=180,y=250)
    
        def CONFIGURACION():
              print('Oprimo conf')
              self.ventana_edit = False
              self.frame_3.place(x=1, y=0)
              self.frame_4.place(x=1, y=100000)

        def mouseClick9(event):
              print('Oprimo9')
              self.button1['bg']= 'green2'
              
              
        def mouseClick10(event):
              print('Oprimo10')
              self.button1['bg']= 'white'
              if(self.ventana_edit == False):
                    #self.frame_3.place(x=1, y=100000)
                    self.frame_4.place(x=1, y=0)
                    self.ventana_edit = True
              else:
                    CONFIGURACION()
              None
       
        image2 = Img.open('pixlr-bg-result.png')#ZWOL_LOGO.png
        image2 = image2.resize((100,50), Img.Resampling.LANCZOS)
        img2= ImageTk.PhotoImage(image2)
 
        self.button1= Label( self.root,font= ('Helvetica 9 '),image=img2, compound= LEFT)#, text="CONFIGURACION" 
        self.button1.place(x=10, y=746)
        self.button1.bind( "<Button>",mouseClick9 )    
        self.button1.bind("<ButtonRelease-1>",mouseClick10)
        self.button1['bg']= 'white'

        
        ''' CONFIGURACION DE SALIDAS '''
          
        def BUT_1(event):
              global comparo
              if (self.BUT_OUT1['bg']== 'green2'):
                    self.BUT_OUT1['bg']= 'red'
                    self.OUT_1 = False
                    set_out(15,0)# llamo a la funcion set_out del diccionario y configuro la salida 
              else:
                    self.BUT_OUT1['bg']= 'green2'
                    self.OUT_1 = True
                    set_out(15,1)
                    
        def BUT_2(event):
              global comparo
              if (self.BUT_OUT2['bg']== 'green2'):
                    self.BUT_OUT2['bg']= 'red'
                    self.OUT_2 = False
                    set_out(14,0)
                    
              else:
                    self.BUT_OUT2['bg']= 'green2'
                    self.OUT_2 = True
                    set_out(14,1)
                    
                    
        def BUT_3(event):
              if (self.BUT_OUT3['bg']== 'green2'):
                    self.BUT_OUT3['bg']= 'red'
                    self.OUT_3 = False
                    set_out(13,0)
              else:
                    self.BUT_OUT3['bg']= 'green2'
                    self.OUT_3 = True
                    set_out(13,1)
                    
        def BUT_4(event):
              if (self.BUT_OUT4['bg']== 'green2'):
                    self.BUT_OUT4['bg']= 'red'
                    self.OUT_4 = False
                    set_out(12,0)
              else:
                    self.BUT_OUT4['bg']= 'green2'
                    self.OUT_4 = True
                    set_out(12,1)
                    
        def BUT_5(event):
              if (self.BUT_OUT5['bg']== 'green2'):
                    self.BUT_OUT5['bg']= 'red'
                    self.OUT_5 = False
                    set_out(11,0)
              else:
                    self.BUT_OUT5['bg']= 'green2'
                    self.OUT_5 = True
                    set_out(11,1)
                    
        def BUT_6(event):
              if (self.BUT_OUT6['bg']== 'green2'):
                    self.BUT_OUT6['bg']= 'red'
                    self.OUT_6 = False
                    set_out(10,0)
              else:
                    self.BUT_OUT6['bg']= 'green2'
                    self.OUT_6 = True
                    set_out(10,1)
                    
        def BUT_7(event):
              if (self.BUT_OUT7['bg']== 'green2'):
                    self.BUT_OUT7['bg']= 'red'
                    self.OUT_7 = False
                    set_out(9,0)
              else:
                    self.BUT_OUT7['bg']= 'green2'
                    self.OUT_7 = True
                    set_out(9,1)
                    
        def BUT_8(event):
              if (self.BUT_OUT8['bg']== 'green2'):
                    self.BUT_OUT8['bg']= 'red'
                    self.OUT_8 = False
                    set_out(8,0)
              else:
                    self.BUT_OUT8['bg']= 'green2'
                    self.OUT_8 = True
                    set_out(8,1)

                    

        #-------OUT 1---------#            
        self._out_1 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 0 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_1.place(x=280, y=42)

        self.BUT_OUT1 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT1.place(x=400, y=40)

        self.BUT_OUT1.bind( "<Button>",BUT_1 )
        self.BUT_OUT1['bg']= 'red'
        #-------OUT 2---------#            
        self._out_2 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 1 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_2.place(x=280, y=72)

        self.BUT_OUT2 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT2.place(x=400, y=70)

        self.BUT_OUT2.bind( "<Button>",BUT_2 )
        self.BUT_OUT2['bg']= 'red'
        #-------OUT 3---------#            
        self._out_3 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 2 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_3.place(x=280, y=102)

        self.BUT_OUT3 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT3.place(x=400, y=100)

        self.BUT_OUT3.bind( "<Button>",BUT_3 )
        self.BUT_OUT3['bg']= 'red'
        #-------OUT 4---------#            
        self._out_4 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 3 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_4.place(x=280, y=132)

        self.BUT_OUT4 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT4.place(x=400, y=130)

        self.BUT_OUT4.bind( "<Button>",BUT_4 )
        self.BUT_OUT4['bg']= 'red'
        #-------OUT 5---------#            
        self._out_5 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 4 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_5.place(x=280, y=162)

        self.BUT_OUT5 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT5.place(x=400, y=160)

        self.BUT_OUT5.bind( "<Button>",BUT_5 )
        self.BUT_OUT5['bg']= 'red'
        #-------OUT 6---------#            
        self._out_6 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 5 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_6.place(x=280, y=192)

        self.BUT_OUT6 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT6.place(x=400, y=190)

        self.BUT_OUT6.bind( "<Button>",BUT_6 )
        self.BUT_OUT6['bg']= 'red'
        #-------OUT 7---------#            
        self._out_7 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 6 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_7.place(x=280, y=222)

        self.BUT_OUT7 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT7.place(x=400, y=220)

        self.BUT_OUT7.bind( "<Button>",BUT_7 )
        self.BUT_OUT7['bg']= 'red'
        #-------OUT 8---------#            
        self._out_8 = Label(self.frame_3, font=("helvetica", 9, "bold"),text = " OUT 7 ", height=1, width=16, bg='white', relief = 'ridge')
        self._out_8.place(x=280, y=252)

        self.BUT_OUT8 = Label( self.frame_3, text="SET" , height=1, width=8)    
        self.BUT_OUT8.place(x=400, y=250)

        self.BUT_OUT8.bind( "<Button>",BUT_8 )
        self.BUT_OUT8['bg']= 'red'

        def mouseClick50(event):
              self.button3['bg']= 'green2'
              print('Oprimo50')
        def mouseClick51(event):
              self.button3['bg']= 'white'
              self.frame_4.place(x=1, y=100000)
              self.frame_3.place(x=1, y=0)
              self.button1.place(x=10, y=746)
              print('Oprimo51')
   
        
        recuperado = recuperar_puntajes("IO/IO.csv")      

              
        image3 = Img.open('pixlr-bg-result.png')#ZWOL_LOGO.png
        image3 = image3.resize((100,50), Img.Resampling.LANCZOS)
        img3= ImageTk.PhotoImage(image3)
 
        self.button3= Label( self.frame_4,font= ('Helvetica 9 '),image=img3, compound= LEFT)#, text="CONFIGURACION" 
        self.button3.place(x=10, y=746)
        self.button3.bind( "<Button>",mouseClick50 )    
        self.button3.bind("<ButtonRelease-1>",mouseClick51)
        self.button3['bg']= 'white'

        self.in_1 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[0]), height=1, width=5, bg='white', relief = 'flat')
        self.in_1.place(x=1, y=10)

        self.in_1e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_1e.place(x=60, y=10)

        self.in_1e.delete(0, 'end')
        self.in_1e.insert(0,str(recuperado[1]))
        

        

        self.in_2 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[2]), height=1, width=5, bg='white', relief = 'flat')
        self.in_2.place(x=1, y=40)

        self.in_2e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_2e.place(x=60, y=40)

        self.in_2e.delete(0, 'end')
        self.in_2e.insert(0,str(recuperado[3]))

        

        self.in_3 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[4]), height=1, width=5, bg='white', relief = 'flat')
        self.in_3.place(x=1, y=70)
        
        self.in_3e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_3e.place(x=60, y=70)

        self.in_3e.delete(0, 'end')
        self.in_3e.insert(0,str(recuperado[5]))

        

        self.in_4 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[6]), height=1, width=5, bg='white', relief = 'flat')
        self.in_4.place(x=1, y=100)

        self.in_4e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_4e.place(x=60, y=100)

        self.in_4e.delete(0, 'end')
        self.in_4e.insert(0,str(recuperado[7]))

        

        self.in_5 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[8]), height=1, width=5, bg='white', relief = 'flat')
        self.in_5.place(x=1, y=130)

        self.in_5e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_5e.place(x=60, y=130)

        self.in_5e.delete(0, 'end')
        self.in_5e.insert(0,str(recuperado[9]))

        self.in_6 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[10]), height=1, width=5, bg='white', relief = 'flat')
        self.in_6.place(x=1, y=160)

        self.in_6e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_6e.place(x=60, y=160)

        self.in_6e.delete(0, 'end')
        self.in_6e.insert(0,str(recuperado[11]))
        

        self.in_7 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[12]), height=1, width=5, bg='white', relief = 'flat')
        self.in_7.place(x=1, y=190)

        self.in_7e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_7e.place(x=60, y=190)

        self.in_7e.delete(0, 'end')
        self.in_7e.insert(0,str(recuperado[13]))

        self.in_8 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[14]), height=1, width=5, bg='white', relief = 'flat')
        self.in_8.place(x=1, y=220)

        self.in_8e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.in_8e.place(x=60, y=220)

        self.in_8e.delete(0, 'end')
        self.in_8e.insert(0,str(recuperado[15]))




        self.out_1 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[16]), height=1, width=5, bg='white', relief = 'flat')
        self.out_1.place(x=250, y=10)

        self.out_1e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_1e.place(x=310, y=10)

        self.out_1e.delete(0, 'end')
        self.out_1e.insert(0,str(recuperado[17]))
        

        

        self.out_2 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[18]), height=1, width=5, bg='white', relief = 'flat')
        self.out_2.place(x=250, y=40)

        self.out_2e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_2e.place(x=310, y=40)

        self.out_2e.delete(0, 'end')
        self.out_2e.insert(0,str(recuperado[19]))

        

        self.out_3 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[20]), height=1, width=5, bg='white', relief = 'flat')
        self.out_3.place(x=250, y=70)
        
        self.out_3e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_3e.place(x=310, y=70)

        self.out_3e.delete(0, 'end')
        self.out_3e.insert(0,str(recuperado[21]))

        

        self.out_4 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[22]), height=1, width=5, bg='white', relief = 'flat')
        self.out_4.place(x=250, y=100)

        #self.out_4e =Label(self.frame_4,font=("Lucida Console", 9),text = str(recuperado[23]), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        #self.out_4e.place(x=310, y=100)

        self.out_4e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_4e.place(x=310, y=100)

        self.out_4e.delete(0, 'end')
        self.out_4e.insert(0,str(recuperado[23]))

        

        self.out_5 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[24]), height=1, width=5, bg='white', relief = 'flat')
        self.out_5.place(x=250, y=130)

        self.out_5e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_5e.place(x=310, y=130)

        self.out_5e.delete(0, 'end')
        self.out_5e.insert(0,str(recuperado[25]))

        self.out_6 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[26]), height=1, width=5, bg='white', relief = 'flat')
        self.out_6.place(x=250, y=160)

        self.out_6e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_6e.place(x=310, y=160)

        self.out_6e.delete(0, 'end')
        self.out_6e.insert(0,str(recuperado[27]))
        

        self.out_7 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[28]), height=1, width=5, bg='white', relief = 'flat')
        self.out_7.place(x=250, y=190)

        self.out_7e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_7e.place(x=310, y=190)

        self.out_7e.delete(0, 'end')
        self.out_7e.insert(0,str(recuperado[29]))

        self.out_8 = Label(self.frame_4, font=("helvetica", 12, "bold"),text = str(recuperado[30]), height=1, width=5, bg='white', relief = 'flat')
        self.out_8.place(x=250, y=220)

        #self.out_8e =Label(self.frame_4,font=("Lucida Console", 9),text = str(recuperado[31]), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        #self.out_8e.place(x=310, y=220)


        
        self.out_8e =Entry(self.frame_4,font=("Lucida Console", 9), width=16,relief = 'flat', bg='lightgreen',justify='center')#.format(N53)
        self.out_8e.place(x=310, y=220)
        self.out_8e.delete(0, 'end')
        self.out_8e.insert(0,str(recuperado[31]))
        
        self._in_1['text']=str(recuperado[1])
        self._in_2['text']=str(recuperado[3])
        self._in_3['text']=str(recuperado[5])
        self._in_4['text']=str(recuperado[7])
        self._in_5['text']=str(recuperado[9])
        self._in_6['text']=str(recuperado[11]) 
        self._in_7['text']=str(recuperado[13])
        self._in_8['text']=str(recuperado[15])
        
        self._out_1['text']=str(recuperado[17])
        self._out_2['text']=str(recuperado[19])
        self._out_3['text']=str(recuperado[21])
        self._out_4['text']=str(recuperado[23])
        self._out_5['text']=str(recuperado[25])
        self._out_6['text']=str(recuperado[27])
        self._out_7['text']=str(recuperado[29])
        self._out_8['text']=str(recuperado[31])

        ''' CONFIGURACION DE SALIDAS '''
        def mouseClick52(event):
              self.button4['bg']= 'green2'

              valores = ("O0 "+ str( self.in_1e.get())+' '), ("O1 "+ str( self.in_2e.get())+' '), ("O2 "+ str( self.in_3e.get())+' '), ("O3 "+
                              str( self.in_4e.get())+' '), ("O4 " + str( self.in_5e.get())+' '), ("O5 " + str( self.in_6e.get())+' '), ("O6 " +
                              str( self.in_7e.get())+' '),("O7 " + str( self.in_8e.get())+' '),(''),("I0 "+ str( self.out_1e.get())+' '), ("I1 "+
                              str( self.out_2e.get())+' '), ("I2 "+ str( self.out_3e.get())+' '), ("I3 "+
                              str( self.out_4e.get())+' '), ("I4 " + str( self.out_5e.get())+' '), ("I5 " + str( self.out_6e.get())+' '), ("I6 " +
                              str( self.out_7e.get())+' '),("I7 " + str( self.out_8e.get())+' ')

              #nombreCarpeta = self.ProgEntryField.get()
              #print('ruta ',nombreCarpeta)
              #Prog= str(self.ProgEntryField.get())
              #directorio = list(str(Prog).split("/") )
              #data_=( '/' .join(directorio[:-1]))
              guardar_puntajes("IO/IO.csv", valores)

        def mouseClick53(event):
              self.button4['bg']= 'white'
              #nombreCarpeta = self.ProgEntryField.get()
              #Prog= str(self.ProgEntryField.get())
              #directorio = list(str(Prog).split("/") )
              #data_=( '/' .join(directorio[:-1]))
              recuperado = recuperar_puntajes("IO/IO.csv")

              self._in_1['text']=str(recuperado[1])
              self._in_2['text']=str(recuperado[3])
              self._in_3['text']=str(recuperado[5])
              self._in_4['text']=str(recuperado[7])
              self._in_5['text']=str(recuperado[9])
              self._in_6['text']=str(recuperado[11]) 
              self._in_7['text']=str(recuperado[13])
              self._in_8['text']=str(recuperado[15])
              
              self._out_1['text']=str(recuperado[17])
              self._out_2['text']=str(recuperado[19])
              self._out_3['text']=str(recuperado[21])
              self._out_4['text']=str(recuperado[23])
              self._out_5['text']=str(recuperado[25])
              self._out_6['text']=str(recuperado[27])
              self._out_7['text']=str(recuperado[29])
              self._out_8['text']=str(recuperado[31])

              self.in_1e.delete(0, 'end')
              self.in_1e.insert(0,str(recuperado[1]))
              self.in_2e.delete(0, 'end')
              self.in_2e.insert(0,str(recuperado[3]))
              self.in_3e.delete(0, 'end')
              self.in_3e.insert(0,str(recuperado[5]))
              self.in_4e.delete(0, 'end')
              self.in_4e.insert(0,str(recuperado[7]))
              self.in_5e.delete(0, 'end')
              self.in_5e.insert(0,str(recuperado[9]))
              self.in_6e.delete(0, 'end')
              self.in_6e.insert(0,str(recuperado[11]))
              self.in_7e.delete(0, 'end')
              self.in_7e.insert(0,str(recuperado[13]))
              self.in_8e.delete(0, 'end')
              self.in_8e.insert(0,str(recuperado[15]))

              self.out_1e.delete(0, 'end')
              self.out_1e.insert(0,str(recuperado[17]))
              self.out_2e.delete(0, 'end')
              self.out_2e.insert(0,str(recuperado[19]))
              self.out_3e.delete(0, 'end')
              self.out_3e.insert(0,str(recuperado[21]))
              self.out_4e.delete(0, 'end')
              self.out_4e.insert(0,str(recuperado[23]))
              self.out_5e.delete(0, 'end')
              self.out_5e.insert(0,str(recuperado[25]))
              self.out_6e.delete(0, 'end')
              self.out_6e.insert(0,str(recuperado[27]))
              self.out_7e.delete(0, 'end')
              self.out_7e.insert(0,str(recuperado[29]))
              self.out_8e.delete(0, 'end')
              self.out_8e.insert(0,str(recuperado[31]))

        self.button4= Label( self.frame_4,font= ('Helvetica 11 '),text = str('REFRESH'), compound= LEFT)#, text="CONFIGURACION" 
        self.button4.place(x=250, y=246)
        self.button4.bind( "<Button>",mouseClick52 )    
        self.button4.bind("<ButtonRelease-1>",mouseClick53)
        self.button4['bg']= 'white'


        #self.3W2<Q=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_1R.place(x=10,y=800)

        #self.li_2R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_2R.place(x=10,y=800)

        #self.li_3R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_3R.place(x=60,y=800)

        #self.li_4R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_4R.place(x=110,y=800)

        #self.li_5R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_5R.place(x=170,y=800)

        #self.li_6R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_6R.place(x=220,y=800)

        #self.li_7R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_7R.place(x=270,y=800)

        #self.li_8R=Label(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        #self.li_8R.place(x=320,y=800)



        
        
        self.li_1_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_1_.place(x=60,y=800)

        

        self.li_2_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_2_.place(x=110,y=800)

        

        self.li_3_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_3_.place(x=160,y=800)

        

        self.li_4_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_4_.place(x=210,y=800)

        

        self.li_5_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_5_.place(x=260,y=800)

        

        self.li_6_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_6_.place(x=310,y=800)

        self.li_7_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_7_.place(x=360,y=800)

        self.li_8_=Text(self.root,font=("Helvetica", 8,"bold"), height=1, width=2, relief = 'sunken')
        self.li_8_.place(x=410,y=800)
        

        ################################################################
        ################################################################
        ################################################################

        self.root.mainloop()
app = Soft()
