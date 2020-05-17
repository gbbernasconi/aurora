#/usr/bin/env python
import serial
import time
import struct
import binascii

ser = serial.Serial(
 port='/dev/ttyUSB0',
 baudrate = 19200,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
counter=0
data=2,78,05,00,00,00,00,00,188,221
txData=struct.pack("B"*len(data), *data)
print binascii.hexlify(txData)
print bin(int(binascii.hexlify(txData),16))
ser.write(txData)
rxData=ser.read(8)
data=struct.unpack("B"*len(rxData), rxData)
print len(data)
for x in data:
 print(x)
