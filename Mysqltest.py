#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sensors used
# 28.6FEAC7000000   ute
# 28.99D3B7010000  inne
# 
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

import string, os
import MySQLdb
#import mysql.connector
#from mysql.connector import errorcode
import sys
import time
import re
from byteport.clients import ByteportHttpClient
import socket
import fcntl
import struct

timefmt = '%Y-%m-%d %H:%M:%S'

NAMESPACE = "GoldenSpace"
API_KEY = "b43cb5709b37ff3125195b54"
POLL_INTERVAL = 30
SHIP_HW_ADDR = "b8:27:eb:4f:4d:d8"	 # <====== FIXA
uid = "Digilinus" # Set default value

DB_NAME = 'Digitemp'

# Connect to the database
try:
  cxn=MySQLdb.connect(host="localhost",user="Digitemp",passwd="Digitemp", db="Digitemp")
  cursor=cxn.cursor()
  print "Database connected"
except cxn.Error, e:
  print "Problem connecting to database"
  sys.exit(-1)
try:
  cursor.execute("CREATE TABLE IF NOT EXISTS Digitemp(dtKey INT PRIMARY KEY NOT NULL AUTO_INCREMENT,\
	DTimeStamp timestamp NOT NULL,\
	OutTemp decimal(3,1) NOT NULL,\
	InTemp decimal(3,1) NOT NULL)")
#	ENGINE=InnoDB)")
  print "Table created"
except cxn.Error, err:
  print("Failed creating table: {}".format(err))
  sys.exit(-1)


# SensorList [SensorName, FileName, Temperature value (set default)]
SensorList = ['OutTemp', '/mnt/1wire/28.5BE8C7000000/temperature', -99,
              'OutTemp', '/mnt/1wire/28.6FEAC7000000/temperature', -99,
              'InTemp', '/mnt/1wire/28.99D3B7010000/temperature', -99]

# SensorList = ['TestSensor', '/mnt/1wire/28.5BE8C7000000/temperature', -99,
#              'OutTemp', '/mnt/1wire/28.6FEAC7000000/temperature', -99,
#              'InTemp', '/mnt/1wire/28.99D3B7010000/temperature', -99]


print(" -----------------------------------------------------")
print("  %s  " % ("Defined sensors"))
print("  %-8s  %s" % ( SensorList[0], SensorList[1]))
print("  %-8s  %s" % ( SensorList[3], SensorList[4]))
print("  %-8s  %s" % ( SensorList[6], SensorList[7]))
print(" -----------------------------------------------------")
print
#client = ByteportHttpClient(NAMESPACE, API_KEY, uid, initial_heartbeat=False)

# print header for results table
print("  Sensor ID  | Date                      | Temperature")
print(" -----------------------------------------------------") 
     # Add the reading to the database

sql = "INSERT INTO Digitemp SET OutTemp=12.1, InTemp=-12.8"
#sqltime = time.strftime( timefmt, time.localtime(int(S[2])))

sqltime = time.localtime
cursor.execute( sql );
# Add the reading to the database

                                                                                                                                           
while True:
  now = time.strftime("%c") #Read time
#Read  Test-sensor
  Idx = 0
  SensorName = SensorList[Idx]
  FileName = SensorList[Idx+1]
  try: 
    file = open(FileName)
  except:
    SensorList[Idx+2] = -99
  else:
    SensorList[Idx+2] = float(file.readline())
    file.close()
    #temp = float(temp) 
    #SensorList[Idx+2] = temp #Store read value
    #client.store({SensorName: temp})
# Read Outdoor sensor
  Idx = 3
  SensorName = SensorList[Idx]
  FileName = SensorList[Idx+1]
  try: 
    file = open(FileName)
  except:
    SensorList[Idx+2] = -99
  else:
    SensorList[Idx+2] = float(file.readline())
    file.close()
    #temp = float(temp)
    #SensorList[Idx+2] = temp #Store read value
    #client.store({SensorName: temp})
# Read Outdoor sensor
  Idx = 6
  SensorName = SensorList[Idx]
  FileName = SensorList[Idx+1]
  try: 
    file = open(FileName)
  except:
    SensorList[Idx+2] = -99
  else:
    SensorList[Idx+2] = float(file.readline())
    file.close()
    #temp = float(temp)
    #SensorList[Idx+2] = temp #Store read value
    #client.store({SensorName: temp})
# Print all read values
  i = 0
  while i < 3 :
    if SensorList[3*i+2] != -99: 
      print("  %s     %s    %.2f" % (SensorList[3*i], now, SensorList[3*i+2]))
      #client.store({SensorList[3*i]: SensorList[3*i+2]}) 
    i = i + 1

  time.sleep(1800)

# quit python script
sys.exit(0)


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
