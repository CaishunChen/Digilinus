set terminal png transparent color
set xdata time
set timefmt "%Y%m%d%H%M"
set format x "%d %b\n%H:%M"
set nokey
set title "Temperature - (4 weeks - 28 days)"
set ylabel "temperature (C)"
set xlabel "date - time"
set grid
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
plot '< ./mysqldata28.sh' using 1:2 with lines 1, '< ./mysqldata28.sh' using 1:3 with lines 1
