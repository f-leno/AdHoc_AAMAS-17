#Stops all HFO related Processes
echo "Stop all HFO related processes"

pkill -f python\ exp*
pkill -f python\ /home/ruben/playground/HFO*
killall -9 rcssserver
#pkill -f  sh\ ru*
echo "Start experiments"
#sh runSimpleExpServerRuben.sh 22445 10 > log/serverAdHocVisitAction.log &
#sleep 5
#sh runSimpleExpAgentRuben.sh 22445 AdHocVisitAction 1 10 > log/logAdHocVisitAction.log &

#sh runSimpleExpServerRuben.sh 23445 10 > log/serverAdHocVisitAction.log &
#sleep 5
#sh runSimpleExpAgentRuben.sh 23445 AdHocVisitAction 11 20 > log/logAdHocVisitAction.log &

#sh runSimpleExpServerRuben.sh 24445 10 > log/serverAdHocVisitAction.log &
#sleep 5
#sh runSimpleExpAgentRuben.sh 24445 AdHocVisitAction 21 30 > log/logAdHocVisitAction.log &

#sh runSimpleExpServerRuben.sh 25445 10 > log/serverAdHocVisitAction.log &
#sleep 5
#sh runSimpleExpAgentRuben.sh 25445 AdHocVisitAction 31 40 > log/logAdHocVisitAction.log &

#sh runSimpleExpServerRuben.sh 26445 10 > log/serverAdHocVisitAction.log &
#sleep 5
#sh runSimpleExpAgentRuben.sh 26445 AdHocVisitAction 41 50 > log/logAdHocVisitAction.log &

# --

sh runSimpleExpServerRuben.sh 32945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 32945 AdHocVisitAction 1 5 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 33945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 33945 AdHocVisitAction 11 15 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 34945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 34945 AdHocVisitAction 21 25 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 35945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 35945 AdHocVisitAction 31 35 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 36945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 36945 AdHocVisitAction 41 45 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 22945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 22945 AdHocVisitAction 6 10 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 23945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 23945 AdHocVisitAction 16 20 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 24945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 24945 AdHocVisitAction 26 30 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 25945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 25945 AdHocVisitAction 36 40 > log/logAdHocVisitAction.log &

sh runSimpleExpServerRuben.sh 26945 5 > log/serverAdHocVisitAction.log &
sleep 5
sh runSimpleExpAgentRuben.sh 26945 AdHocVisitAction 46 50 > log/logAdHocVisitAction.log &
