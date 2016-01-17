#!/bin/sh
 # this is a GNUPLOT script to take the website download data and create a
 #  graphical overview png file
 #
 # Parkview August 2009

 # Local Variables
 BASEDIR="/var/www/html"
 #BASEDIR="/usr/local/apache2/htdocs/"
 DATAFILE_IN="/home/arne/Digilinus/SQLData/sqldata_month.dat"
 MINDATAFILE_IN="/tmp/gnuplot-data-min.dat"
 MAXDATAFILE_IN="/tmp/gnuplot-data-max.dat"
 SRISEDATAFILE_IN="/tmp/gnuplot-data-srise.dat"
 SSETDATAFILE_IN="/tmp/gnuplot-data-sset.dat"
 PNG="$BASEDIR/OutTempMonth.png"

 MINY=13
 MAXY=41
 MYTICS=2
 COLOR1="#CD2222"
 COLOR2="#CD9F22"
 COLOR3="#2225CD"
 COLOR5="#f24D97"
 COLOR4="#000066"
 COLOR6="#22fDd7"
 COLOR7="#22fD57"
 COLOR8="#225D57"
 COLOR9="#72aDa7"
 COLOR10="#000000"
 COLOR11="#666666"

 # extract the required data from the csv file
 EDATE=`tail -1 $DATAFILE_IN | cut -d"," -f1`
 SDATE=`head -2 $DATAFILE_IN | tail -1 | cut -d"," -f1`

 # Now go and plot the graph
 /usr/bin/gnuplot << EOF
 set datafile separator ","
 set style fill solid border -1
 set style line 1 lt 2 lw 1
 set pointsize .5
 set sample 45
 set terminal png size 1024,400
 set terminal png
 set terminal png transparent
 set output "$PNG"
 #set xlabel "Date - Time"
 set ylabel "Degree C"
 set y2label "Degree C"
 #set title "Outside - Temperature [C]"
 set xdata time
 set timefmt "%Y-%m-%d %H:%M:%S"
 set timestamp "Generated %Y-%m-%d %H:%M"
 set format x "%d %h\n%H:%M"
 #set xrange [ "$SDATE":"$EDATE" ]
 set xrange [ "$EDATE":"$SDATE" ]
 set timefmt "%Y-%m-%d %H:%M:%S"
 set yrange [ * : * ]
 #set yrange [ $MINY : $MAXY ]
 set xtics border out scale 2
 set ytics out mirror $MYTICS
 set y2tics out mirror $MYTICS
 set mxtics 4
 set mytics 2
 set grid x y
 #plot "$DATAFILE_IN"  using 1:7 title "Outside-average" smooth bezier, "" using 1:7 title "Outside" with lines lc rgb "$COLOR3", "" using 1:6 title "Attic" with lines lc rgb "$COLOR8","" using 1:3 title "Attic Switch" with lines lc rgb "$COLOR9", "$MAXDATAFILE_IN"  using 1:2 title "Max Temp"  with points pointtype 6 pointsize 2 lc rgb "$COLOR1", "$MINDATAFILE_IN"  using 1:2 title "Min Temp"  with points pointtype 6 pointsize 2 lc rgb "$COLOR4", "$SRISEDATAFILE_IN"  using 1:2 title "Sunrise"  with points pointtype 24 pointsize 1 lc rgb "$COLOR11", "$SSETDATAFILE_IN"  using 1:2 title "Sunset"  with points pointtype 24 pointsize 1 lc rgb "$COLOR10"
 plot "$DATAFILE_IN"  using 1:2 title "Outside" with lines lc rgb "$COLOR3", "" using 1:3 title "Indoor" with lines lc rgb "$COLOR2"
EOF