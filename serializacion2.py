
#! /usr/bin/env python
# encoding: latin1

import csv

def guardar_puntajes(nombre_archivo, puntajes):
    
    Prog=str(nombre_archivo)
    #print('Nombre de archivo ',Prog)
    with open(Prog, 'w') as f:
              data_=( '\n' .join(puntajes))
              f.write(data_+'\n')
              f.close()
                  

def recuperar_puntajes(nombre_archivo):
    Prog=str(nombre_archivo)
    #print('Nombre de archivo ',Prog)
    f = open(nombre_archivo, "r")
    puntajes = []
    def format_word_2(string):
            return str(string)
    def line_2_values(words):
            values = []        
            for word in words:
                  try:
                        number = float(word)
                        values.append(number)
                  except:
                        pass
            return values
    def line_3_values(string):
            
            values_2 = []        
            for strin in string:
                  try:
                        number = str(strin)
                        values_2.append(number)
                  except:
                        pass
            return values_2
    for linea in f:    
        #-----------------------------------------------------------------------
        # Busca palabra "*"
        #-----------------------------------------------------------------------           
        linecmd = linea
        words = linecmd.split(' ')
        string = linecmd.split(' ')
        values = line_2_values(words)
        values_2= line_3_values(string)
        nvalues_2 = len(values_2)

         
        if linecmd == "  ":
                  return
        elif( nvalues_2 >= 3):    
            
            for i in range(-1, 1):
                ss=format_word_2(values_2[i + 1])
                puntajes.append(ss)
                #print(ss)
    return puntajes
#recuperado = recuperar_puntajes("/home/robot/Escritorio/zwol_cartesiano_gruapa (modbus)/Programas/ZWOL/IO/IO.csv")
#print(recuperado)

