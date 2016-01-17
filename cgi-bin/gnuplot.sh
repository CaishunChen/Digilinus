#!/bin/sh
# Here's the Content-type line to tell the browser that this reply
# is a png image.
#echo Content-type: image/png 

# Here's the header/content blank separation line required by Apache
#echo
#/usr/bin/gnuplot test.gnu

/usr/bin/gnuplot << ENDOFINPUT
set terminal png 
#set terminal x11
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d %b\n%H:%M"
set timestamp "generated on %Y-%m-%d %H:%M"
set title "Temperature - 7 days"
set ylabel "Temp (C)"
set xlabel "date - time"
set grid
set key
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
#plot "< /var/www/cgi-bin/mysql2gnuplot.pl" using 1:2 with linespoints
plot "< /var/www/cgi-bin/mysqldata.sh" using 1:4 title "ute" with lines, "<  /var/www/cgi-bin/mysqldata.sh" using 1:3 title "inne" with lines
ENDOFINPUT
