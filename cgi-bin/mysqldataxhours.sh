#!/bin/sh
host=192.168.1.90
database=digitemp
user=digitemp
pass=digitemp
#
#
echo "SELECT time, temp1, temp2 FROM digitemp WHERE (time > DATE_SUB(NOW(),INTERVAL $1 HOUR)) ORDER BY time DESC;" | mysql --host=$host --database=$database --user=$user --pass=$pass --silent
