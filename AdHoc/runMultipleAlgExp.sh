# $1 port
# $2 Agent class 1
# $3 Agent Class 2
# $4 Agent Class 3
# $5 initial repetition
# $6 final repetition
# $7 log folder


for I in $(seq $5 1 $6)
do
	python experiment.py -t 5000 -d 100 -r $I -i 20 -a1 $2 -a2 $3 -a3 $4 -p $1 -l $7
	sleep 20
done



