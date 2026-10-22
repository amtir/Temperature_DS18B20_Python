#!/usr/bin/python3

'''
Aim, Purpose, Taget: 

This Python-script reads/measures the temperature from four sensors.
 
Sensor-Type: DS1820 1 Wire-temperature Sensor
Protocol-type: 1-Wire interface bus

Programmer: Ak. MT.
Date: 21-01-2019

'''

import re, os, time 
from lib_python_logging import * 

#-----------------------------------------------------
# Function: reads and parses the DS1820 sensor data file
# @input: String path to the DS1820 Sensor file.
# @Output: Returns the temperature 
def read_sensor(path):
  value = "U"
  try:
    f = open(path, "r")
    line = f.readline()
    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
      if m:
        value = str(float(m.group(2)) / 1000.0)
    f.close()
  except IOError as  e:
    print (time.strftime("%x %X"), "Error reading", path, ": ", e)
  return value
#-----------------------------------------------------

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(strPath):
    lines = read_temp_raw(strPath)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(strPath)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
#-----------------------------------------------------



# Logger object to log our events, data etc.
my_logger = get_logger("main-temp-sensor")


# List the DS1820 sensors on the 1-wire bus.
# define pathes to 1-wire sensors data
# could be acquired automatically in an ADT.
path_temp1 =  "/sys/bus/w1/devices/28-02049245c24a/w1_slave"
path_temp2 =  "/sys/bus/w1/devices/28-0218924579af/w1_slave"
path_temp3 =  "/sys/bus/w1/devices/28-020592452f77/w1_slave"
path_temp4 =  "/sys/bus/w1/devices/28-02ff9245ffff/w1_slave"
  
 
  

while(True):
  # read temp-sensor1 data
  data = ''
  #for path in pathes: 
  #data = read_sensor(path_temp1) + '[°C]'
  data = str(float(read_temp(path_temp1)[0])) + '[°C]'
  #my_logger.debug("Starting ...")
  my_logger.debug( "Temperature1: " + data )


  # read temp-sensor2 data
  #data = read_sensor(path_temp2) + '[°C]'
  data = str(float(read_temp(path_temp2)[0]) ) + '[°C]'
  my_logger.debug( "Temperature2: " + data )
  #print(data)

  # read temp-sensor3 data
  #data = read_sensor(path_temp3) + '[°C]'
  data = str(float(read_temp(path_temp3)[0]) ) + '[°C]'
  my_logger.debug( "Temperature3: " + data )
  #print(data)
  
  
  # read temp-sensor4 data
  #data = read_sensor(path_temp4) + '[°C]'
  data = str(float(read_temp(path_temp4)[0]) ) + '[°C]'
  my_logger.debug( "Temperature4: " + data )
  #print(data)
  #print("---------------------")
  
  time.sleep(1)
