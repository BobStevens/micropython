# Continuously polls the BMP180 Pressure Sensor
import pyb
import BMP085 

# creating objects
blue = pyb.LED(4)
bmp180 = BMP085.BMP085(port=2,address=0x77,mode=3,debug=False)
while 1:
  blue.toggle()
  temperature = bmp180.readTemperature()
  print("%f celcius" % temperature)    
  pressure = bmp180.readPressure()
  print("%f pascal" % pressure)
  altitude = bmp180.readAltitude()
  print("%f meters" % altitude)
  pyb.delay(100)
