#!/bin/sh
#
# 
echo Start TightVCNserver
service tightvncserver start
echo Start owfs
owfs -uall --usb_regulartime --allow_other /mnt/1wire

#23 Dec 2015 Start now moved to crontab, starts Digilinus at reboot. With log file Digilog.txt
echo start Digilinus
cd /home/arne/Digilinus
./Digilinus.py > Digilog.txt 2>&1&

echo Create first Plot
./ReadSQLAndStoreSensors.py
