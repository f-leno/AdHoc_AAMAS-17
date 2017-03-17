# $1 is the port, $2 the number of repetitions /home/leno/HFO/bin/HFO --offense-agents=3 --defense-npcs=1 --fullstate --headless --trials=33100 --port=$1 --frames-per-trial=200
for I in $(seq 1 1 $2)
do
    /home/ruben/playground/HFO/bin/HFO --no-logging --offense-agents=3 --defense-npcs=1 --fullstate --headless --trials=30100 --port=$1 --frames-per-trial=200
done
