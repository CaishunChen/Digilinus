#!/bin/sh

#timestamp=`date -R`
days=28
#days=$1

# Here's the Content-type line to tell the browser that this reply
# is a png image.
echo Content-type: image/png 

# Here's the header/content blank separation line required by Apache
echo

/usr/bin/gnuplot << ENDOFINPUT
set terminal png transparent
#set terminal x11
set xdata time
#
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d %b\n%H:%M"
set timestamp "Generated %Y-%m-%d %H:%M"
#set timefmt "%Y-%m%d"
#set xrange [ "20060201": "20060301"]
#
#set timefmt "%Y%m%d%H%M"
#set timefmt "%H:%M:%s"
#set format x "%d %b\n%H:%M"
#set format x "%Y%m%d%H%M"
#set format x "%H:%M"
#
#set timestamp "generated on %Y-%m-%d %H:%M by `whoami`"
set timestamp "generated on %Y-%m-%d %H:%M"
#set label "generated on `date +%Y-%m-%d` by `whoami`" at 1,1
#set xrange [ "20060315":"20060321" ]
#
#set title "Temperature - 7 days ($timestamp)"
set title "Temperature - $days days"
set ylabel "temperature (C)"
set xlabel "date\ntime"
set grid
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
#set nokey
#set label "graph middle" at graph .5, .5 rotate
#plot "< ./mysql2gnuplot.pl" using 1:2 with linespoints
#
#plot "< ./mysqldatax.sh 28" using 1:4 title "ute" with lines,\
#"< ./mysqldatax.sh 28" using 1:3 title "inne" with lines
plot "< ./mysqldata.sh" using 1:4 title "ute2" with lines,
"< ./mysqldata.sh" using 1:3 title "inne" with lines
#
#plot "temp.data" using 1:2 title "ute" with lines,\
#     "temp.data" using 1:3 title "inne" with lines
ENDOFINPUT


