#!/usr/bin/env python 
#
# this will extract the relevant temperature data from the DB and plot the data via gnuPlot into a png graph

# This has been updated to suit the new MySQL table that hosts one record for all the sensors
#
#  Parkview 2013-04-05
#

import os
import time
import MySQLdb as mdb
import sys
import subprocess
import datetime, time
import ephem # install from pyephem`


MYSQL_HOST = '192.168.1.90'
MYSQL_DB = "Digitemp"
MYSQL_USER = "Digitemp"
MYSQL_PASSWD = "Digitemp"
MYSQL_TBL_SENSOR = "DigiTable"
MYSQL_TBL_TEMP = "OutTemp"

max_file="/tmp/gnuplot-data-max.dat"
min_file="/tmp/gnuplot-data-min.dat"
srise_file="/tmp/gnuplot-data-srise.dat"
sset_file="/tmp/gnuplot-data-sset.dat"

# lets work out the previous Sun Set and Sun Rise:
o = ephem.Observer()
o.lat, o.long, o.date = '22:12', '65:59', datetime.datetime.utcnow()
sun = ephem.Sun(o)
SRISE=ephem.localtime(o.previous_rising(sun))
SSET=ephem.localtime(o.previous_setting(sun))


# Setup data files, set number of samples == no of days.
file="/home/arne/Digilinus/SQLData/sqldata_last_period.dat"
Data_Limit=100  # = 10 days; 30 min per sample, so 48 per day. 30 days = 1440, 1 year = 17520
#  First need to query the DB for a list of sensor names and compare with what we actually have on the network
try:
    con = mdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, MYSQL_DB);
    cur = con.cursor()
    #print"Database opened ok"
    # go get around days worth of temperature records
    cur.execute("""SELECT DTimeStamp,OutTemp, InTemp FROM DigiTable  order by DTimeStamp desc limit %s""", Data_Limit) 
    f=open(file, 'w')
    for row in cur.fetchall():
       # now lets  add this into a list variable for use
       DATA1=row[0].strftime('%Y-%m-%d %H:%M:%S'),str(row[1]),str(row[2])
       DATA=','.join(DATA1)+'\n'
       f.write(DATA)
      # print  DATA  # could add a strip RH to clear the line feed
    #print " "
    f.close()
    
    file="/home/arne/Digilinus/SQLData/sqldata_month.dat"
    Data_Limit=5000  # = 104 days; 30 min per sample, so 48 per day. 30 days = 1440, 1 year = 17520
    # now lets get the min data so it can be plotted
    cur.execute("""SELECT DTimeStamp,OutTemp, InTemp FROM DigiTable  order by DTimeStamp desc limit %s""", Data_Limit) 
    f=open(file, 'w')
    for row in cur.fetchall():
       # now lets  add this into a list variable for use
       DATA1=row[0].strftime('%Y-%m-%d %H:%M:%S'),str(row[1]),str(row[2])
       DATA=','.join(DATA1)+'\n'
       f.write(DATA)
   
  
   
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)         
finally:  
    if con:      
      con.close()

# call the various gnuPlot scripts from here:
    try:
      subprocess.Popen('/home/arne/Digilinus/PlotLastPeriod.cgi',shell = True)   
    except OSError, e:
      print 'OS Error: '
    try:
      subprocess.Popen('/home/arne/Digilinus/PlotLastMonth.cgi',shell = True)   
    except OSError, e:
      print 'OS Error: '
      
    

#print " Sun Rise: ", SRISE
#print " Sun Set: ", SSET