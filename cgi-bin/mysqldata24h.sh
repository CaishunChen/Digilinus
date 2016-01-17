#!/bin/sh

echo "SELECT time, temp1, temp2 FROM digitemp WHERE (time > DATE_SUB(NOW(),INTERVAL '1' DAY)) ORDER BY time DESC;" | mysql --host=192.168.0.8 --database=digitemp --user=digitemp --pass=digitemp --silent
