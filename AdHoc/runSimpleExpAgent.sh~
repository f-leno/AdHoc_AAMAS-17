# $1 is the port, $2 the agent, and $3 the initial trial  $4 the end trial python experiment.py -t 3000 -d 100 -r $I -i 10 -a1 $2 -a2 $2 -a3 $2 -p $1

for I in $(seq $3 1 $4)
do
	python experiment.py -t 5000 -d 100 -r $I -i 20 -a1 $2 -a2 $2 -a3 $2 -p $1
	sleep 20
done



