#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sensors used
# 28.571AB8010000   ute-stugan
# 28.7EF3FE000000   inne-stugan
#
# Creation:    02.01.2013
# Last Update: 07.04.2015
#
# Copyright (c) 2013-2015 by Georg Kainzbauer <http://www.gtkdb.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# import sys module
# CREATE table digitemp (
#   dtKey int(11) NOT NULL auto_increment,
#   time timestamp NOT NULL,
#   temp1 decimal(3,1) NOT NULL,
#   temp2 decimal(3,1) NOT NULL,
#   PRIMARY KEY (dtKey),
#   KEY time_key (time)
# );
#
# GRANT SELECT,INSERT ON digitemp.* TO digitemp@localhost
# IDENTIFIED BY 'password';

import sys
import string, os
import MySQLdb
timefmt = '%Y-%m-%d %H:%M:%S'
import time
import re
from byteport.clients import ByteportHttpClient
import socket
import fcntl
import struct

# Byteport setup
NAMESPACE = "GoldenSpace"
API_KEY = "b43cb5709b37ff3125195b54"
uid = "Digilinus" # Set default value

# System setup
DEBUG_ON = 'NO'  # For debugging, print temperature, sensors etc
POLL_INTERVAL =  30 # Normally 30 Minutes, to be adjusted!

# Mysql setup
DB_HOST   = 'localhost'
DB_NAME   = 'Digitemp'
DB_USER   = 'Digitemp'
DB_PASSWD = 'Digitemp'
#DB_TABLE  = 'Digitemp'
DB_TABLE  = 'DigiTable'
DB_PORT   = 3333  # Not used now


# Connect to the database
try:
  cxn=MySQLdb.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD, db="Digitemp")
# cxn=MySQLdb.connect(host=DB_HOST,user=DB_USER,passwd=DB_PASSWD, db="Digitemp", port=int(DB_PORT))
  cursor=cxn.cursor()
  print "Database connected"
except cxn.Error, e:
  print "Problem connecting to database"
  sys.exit(-1)


try:
  cursor.execute("CREATE TABLE IF NOT EXISTS DigiTable(dtKey INT PRIMARY KEY NOT NULL AUTO_INCREMENT,\
  DTimeStamp timestamp NOT NULL,\
  OutTemp float(3,1) NOT NULL,\
  InTemp float(3,1) NOT NULL)")
# ENGINE=InnoDB)")
  print "Table defined: ", DB_TABLE
except cxn.Error, err:
  print("Failed creating table: {}".format(err))
  sys.exit(-1)


# SensorList [SensorName, FileName, Temperature value (set default)]
SensorList = ['OutTemp',     '/mnt/1wire/28.571AB8010000/temperature', -99,
              'InTemp',      '/mnt/1wire/28.7EF3FE000000/temperature', -99]


print(" -----------------------------------------------------")
print("  %s  " % ("Defined sensors"))
print("  %-8s  %s" % ( SensorList[0], SensorList[1]))
print("  %-8s  %s" % ( SensorList[3], SensorList[4]))
print(" -----------------------------------------------------")
print
client = ByteportHttpClient(NAMESPACE, API_KEY, uid, initial_heartbeat=False)

# print header for results table
print("  Date                     |   Sensor  |   Temperature")
print(" -----------------------------------------------------")
OutTemp = -99
InTemp  = -99

#while True:
now = time.strftime("%c") #Read time for sensor reading

# Setup filenames etc.
OutSensor = SensorList[0]
OutFileName = SensorList[1]
InSensor = SensorList[3]
InFileName = SensorList[4]
# Read Outdoor sensor
OutTemp = -99
try:
  MyFile = open(OutFileName)
except:
  print ("Unable to open file: ", OutFileName)  

try:
  OutTemp = float(MyFile.readline())
  MyFile.close()
except:
  MyFile.close()

  # Read Indoor sensor
InTemp = -99
try:
  MyFile = open(InFileName)
except:
  print ("Unable to open file: ", InFileName)     

try:
  InTemp = float(MyFile.readline())
  MyFile.close()
except:
  MyFile.close()

# Print all temperature values, debug purpose...
  #print("Pre-  %s     %s    %+4.2f" % (now, "OutTemp", OutTemp))
  #print("Pre-  %s     %s    %+4.2f" % (now, "InTemp", InTemp))
if OutTemp != -99: 
#    print("  %s     %s    %+4.1f" % (now, "OutTemp", OutTemp))
  try:
    client.store({"OutTemp": OutTemp}) # Store value in Byteport
  except:
    print("Failed storing in Byteport:")
else:
  print("No reading   %s     %s    %+4.1f" % (now, "OutTemp", OutTemp))

if InTemp != -99: 
#    print("  %s     %s    %+4.1f" % (now, "InTemp ", InTemp))
  try:
    client.store({"InTemp": InTemp}) # Store value in Byteport
  except:
    print("Failed storing in Byteport:")
else:
  print("No reading   %s     %s    %+4.1f" % (now, "InTemp ", InTemp))

# Add the reading to the database	
try:
  sql = "INSERT INTO DigiTable (InTemp, OutTemp) VALUES (%+3.1f, %+3.1f)"
  cursor.execute( sql % (InTemp, OutTemp))
  cxn.commit()    		
except cxn.Error, err:
  print("Failed storing in Mysql table: {}".format(err))

# Set poll interval, number of seconds
#  time.sleep(POLL_INTERVAL*60)

# quit python script
sys.exit(0)
