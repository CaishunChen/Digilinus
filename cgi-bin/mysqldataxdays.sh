
#!/bin/sh
host=192.168.1.90
database=digitemp
user=digitemp
pass=digitemp
#
#
echo "SELECT time, temp1, temp2 FROM digitemp WHERE (time > DATE_SUB(NOW(),INTERVAL $1 DAY)) ORDER BY time DESC;" | mysql --host=$host --database=$database --user=$user --pass=$pass --silent
#echo "SELECT time, temp1, temp2 FROM digitemp WHERE (time > DATE_SUB('2008-01-01 00:00:00', INTERVAL, $1 DAY)) ORDER BY time DESC;" | mysql --host=$host --database=$database --user=$user --pass=$pass --silent
