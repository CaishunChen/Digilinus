#!/bin/sh
days=1
# Here's the Content-type line to tell the browser that this reply
# is a png image.
echo Content-type: image/png 

# Here's the header/content blank separation line required by Apache
echo

#/usr/bin/gnuplot test.gnu
/usr/bin/gnuplot << ENDOFINPUT
set terminal png transparent
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set timestamp "Generated %Y-%m-%d %H:%M"
set format x "%d %b\n%H:%M"
set key
set title "Temperature - 24 hours"
set ylabel "Temp (C)"
set xlabel "date - time"
set grid
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
plot "< ./mysqldataxdays.sh $days" using 1:4 title "ute" with lines, "< ./mysqldataxdays.sh $days" using 1:3 title "inne" with lines
ENDOFINPUT