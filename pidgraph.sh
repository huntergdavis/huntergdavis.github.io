#!/bin/sh

if [ $# -ne 3 ]
then
   echo "Error - too few or too many arguments"
   echo "Syntax : $0 pid interval file"
   echo " Use to output cpu usage at interval while pid running, then display in gnuplot"
exit 1
fi

rm -f outplot.plot
rm -f $3

echo "set title \"CPU for PID $1 with interval $2\" " >> $3
echo "set ylabel \"CPU Percentage\" " >> $3
echo "set xlabel \"Time\" " >> $3
echo "set xdata time" >> $3
echo "set timefmt \"%H:%M:%S\" " >> $3
echo "set format x \"%H:%M:%S\" " >> $3
echo "plot 'outplot.plot' using 2:1 with lines" >> $3

RUNN=1

while [ $RUNN -eq 1 ]
do
	PID=`ps -p $1 -o size=`
	if [ -z "$PID" ] ; then 
		echo " PID NO LONGER ACTIVE"
		RUNN=0
	fi
	
	if [ $RUNN -eq 1 ] ; then
		date +%H:%M:%S  > temp2
		ps -p $1 -o pcpu= > temp1
		paste temp1 temp2 >> outplot.plot
		rm temp1 temp2
	fi

	sleep $2

done
gnuplot -persist $3



