#!/bin/sh
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
#set format x "%d %b\n%H:%M"
set format x "%d %b"
set key
set style boxes
set timestamp "Generated %Y-%m-%d %H:%M"
set title "Temperature - Year"
set ylabel "Temp (C)"
#set xlabel "Date"
set grid
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
plot "< ./mysqldataxyear.sh 2010" using 1:3 title "2010" with lines, \
     "< ./mysqldataxyear.sh 2009" using 1:3 title "2009" with lines, \
     "< ./mysqldataxyear.sh 2008" using 1:3 title "2008" with lines, \
     "< ./mysqldataxyear.sh 2007" using 1:3 title "2007" with lines
#     "< ./mysqldataxyear.sh 2006" using 1:4 title "2006" with lines
ENDOFINPUT
