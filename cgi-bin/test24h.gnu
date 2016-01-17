set terminal png transparent
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%d %b\n%H:%M"
set nokey
set title "Temperature - ww24 hours"
set ylabel "Temp (C)"
set xlabel "date - time"
set grid
#set grid ytics
#set grid xtics
#set rmargin 15
#unset key
plot "< ./mysqldatax.sh 28" using 1:4 title "ute" with lines, "< ./mysqldatax.sh 28" using 1:3 title "inne" with lines
