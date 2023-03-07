

import logging
logger = logging.getLogger(__name__)

from struct import pack, unpack

import threading
from pyModbusTCP.client import ModbusClient
import asyncio
import time
import nest_asyncio
nest_asyncio.apply()
STRUCT_SERIALIZERS = {
    'INT8': ('>b', 1),
    'INT16': ('>h', 2),
    'INT32': ('>i', 4),
    'INT24': ('>i', 2),
    'UINT24': ('>I', 2),
    'UINT8': ('>B', 1),
    'UINT16': ('>H', 2),
    'UINT32': ('>I', 4),
}


def serialize(dtype, value):
    struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
    #print('serialize struct_type   ',struct_type)
    return pack(struct_type, value)

def deserialize(dtype, data):
    struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
    #print('deserialize struct_type   ',struct_type)
    return unpack(struct_type, data)[0]       
class Element:
    def __init__(self, name, index, subindex, dtype,acces):
        self.name = name
        self.nombre = name
        #print('name ',self.name)
        self.index = index
        self.subindex = subindex
        self.dtype = dtype
        self.size_bytes = STRUCT_SERIALIZERS.get(dtype)[1]
        self.acces = acces

    def set(self,value,pass_= None):
        #print("SET %s: %s", self.name, bin(value))
        if(self.acces != 'RO' or pass_ == 'admin'):
            self.name = (self.index, self.subindex, serialize(self.dtype, value))
        else:
            #logger.warning("OBJETO SOLO DE LECTURA %=%r",hex(self.index))
            ss = logger.warning("""ERROR !!
Esta intentando escribir un objeto de solo lectura
Objeto (%s = %s)""", self.nombre, hex(self.index))
            
        

    def get(self):
        data = (self.index, self.subindex, self.size_bytes)
        try:
            value = (self.name[2].hex())
        except:
            value = 0

            
        def pad_hex(s,size):
            padded = '0x'
            padded += '0'*((size)-(len(s)))
            
            for i in range(size-2, len(s)):
                padded += s[i]
            #print('padded ',padded)    
            return padded
        #print ( 'value ', value)
        
        value = (pad_hex(str(value),self.size_bytes))[2:]
        base16INT = int(str(value),16)
        value = hex(base16INT)



        return value
        


    
HOMMING_DATA = Element('HOMMING_DATA', 0x9040, 0, 'UINT32','RW')
OUTPUT_OBJECT = Element('OUTPUT_OBJECT', 0x3020, 1, 'UINT16','RW')
INPUT_OBJECT = Element('INPUT_OBJECT', 0x3020, 2, 'UINT16','RO')



HOMMING_DATA.set(1010)
OUTPUT_OBJECT.set(0)
INPUT_OBJECT.set(123,'admin')



TIM_1 = 0.01


global comparo
comparo =[0]

resultado ="000000000000000"
          
def bits(bit_):
        bytes = (ord(b)for b in bit_)
        for b in bytes:
            for i in range(1):
                yield( b >> i)&1  
for b in bits(resultado):
        comparo.append(b)

comparo[0]=0
comparo[1]=0
comparo[2]=0
comparo[3]=0
comparo[4]=0
comparo[5]=0
comparo[6]=0
comparo[7]=0
comparo[8]=0
comparo[9]=0
comparo[10]=0
comparo[11]=0
comparo[12]=0
comparo[13]=0
comparo[14]=0
comparo[15]=0

        
def set_out(indice,valor):
        
                
        def pad_binario_(s):
                padded =''
                padded += '0'*(16-(len(s)))
                for i in range( len(s)):
                    padded += s[i]   
                return (int(padded,2))
        def resultado_boton():
                    global comparo 
                    b=bin(pad_binario_(str(''.join(map(str,comparo)))))
                    num_2 = hex(int(b,2))
                    num_2 = int(num_2,16)
                    OUTPUT_OBJECT.set(num_2)
        comparo[indice]=valor            
        resultado_boton()


        
def bit_in(ss):
      res = bin(int(ss,16))
      def pad_bin(s):
            padded = '0b'
            padded += '0'*(16-(len(s)-2))
            for i in range(2, len(s)):
                  padded += s[i]
            return padded
      def serialize(dtype, value):
            struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
            return pack(struct_type, value)
      def deserialize(dtype, data):
            struct_type = STRUCT_SERIALIZERS.get(dtype)[0]
            return unpack(struct_type, data)[0]
      dtype='UINT16'
      size_bytes = STRUCT_SERIALIZERS.get(dtype)[1]
      num = int(ss,16)
      dat_=serialize(dtype,num)
      dat_2=deserialize(dtype,dat_)

      dat_2 = pad_bin(bin(dat_2))  
      bit_=  list(reversed((dat_2)[2:]))
      return bit_

                            
#-----------------------------------------------------------------------
# Class Software
#-----------------------------------------------------------------------
class Soft(threading.Thread):#object):
      
      
              
      def __init__(self):#, **kwargs):
            self.loop = asyncio.get_event_loop()
            threading.Thread.__init__(self)
            self.start()


      def run(self):
            async def while_loop():
                self.client = ModbusClient(host="192.168.2.137", port=1003, auto_open=True, auto_close=True, timeout=1)# IP DE ARDUINO
            
                
                while True:
     
                    start = time.time() 
                    await asyncio.sleep(TIM_1)


                    regs = self.client.read_holding_registers(0x06040)
                    ss = str((regs)[0])
                    ss = (int(ss))
                    INPUT_OBJECT.set(ss,'admin')

                    ss=OUTPUT_OBJECT.get()
  
                    num_bit = 1
                    resultado = bin(int((ss),16))[2:].zfill(num_bit)
                    def pad_hex(s):
                            padded = ''
                            padded += '0'*(16-(len(s)))
                            
                            for i in range(len(s)):
                                padded += s[i]   
                            return padded

                    pp=pad_hex(resultado)

                    comparo=[]
        
                    def bits(bit_):
                        bytes = (ord(b)for b in bit_)
                        
                        for b in bytes:
                            for i in range(1):
                                yield( b >> i)&1  
                    for b in bits(pp):
                        comparo.append(b)

                    comparo = list(reversed(comparo))

                    if( comparo[0]==1):
                        
                        ss=self.client.write_single_coil(0x000,1)
                    else:
                        self.client.write_single_coil(0x000,0)
                    if( comparo[1]==1):
                        
                        ss=self.client.write_single_coil(0x001,1)
                    else:
                        self.client.write_single_coil(0x001,0)
                    if( comparo[2]==1):
                        
                        ss=self.client.write_single_coil(0x002,1)
                    else:
                        self.client.write_single_coil(0x002,0)
                    if( comparo[3]==1):
                        
                        ss=self.client.write_single_coil(0x003,1)
                    else:
                        self.client.write_single_coil(0x003,0)
                    if( comparo[4]==1):
                        
                        ss=self.client.write_single_coil(0x004,1)
                    else:
                        self.client.write_single_coil(0x004,0)
                    if( comparo[5]==1):
                        
                        ss=self.client.write_single_coil(0x005,1)
                    else:
                        self.client.write_single_coil(0x005,0)
                    if( comparo[6]==1):
                        
                        ss=self.client.write_single_coil(0x006,1)
                    else:
                        self.client.write_single_coil(0x006,0)
                    if( comparo[7]==1):
                        
                        ss=self.client.write_single_coil(0x007,1)
                    else:
                        self.client.write_single_coil(0x007,0)
                        
                
                
                          
                    end = time.time()      
                    TIMER = (end - start)
                    
                    
            self.future = self.loop.create_task(while_loop())
            self.loop.run_until_complete(self.future)


Soft()




