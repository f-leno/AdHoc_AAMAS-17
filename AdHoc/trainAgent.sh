/home/leno/HFO/bin/HFO --no-logging --offense-agents=3 --defense-npcs=1 --fullstate --headless --trials=3003 --port=52345 --frames-per-trial=200 &
sleep 5
python experiment.py -p 52345 -n 3 -a1 SARSATile -a2 SARSATile -a3 SARSATileStorage -t 3000 -i 1500 -d 1 -l /home/leno/HFO/experiments/agentData/

